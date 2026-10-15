# Experiment 6: Establish Secure Remote Login Using SSH

**Course:** COM-511 Network Security Lab  
**Topic:** OpenSSH • Host Identity Verification • Public-Key Authentication  

---

## 1. Overview
This repository contains the configuration workflow, command execution logs, and verification checks for **Experiment 6**. The experiment establishes an encrypted remote administration session between a Windows client and a Kali Linux server over TCP port 22 using the SSHv2 protocol, transitioning from standard password authentication to cryptographic Ed25519 public-key authentication.

---

## 2. Protocol Architecture & Security Concepts
SSH operates across three distinct layers over a reliable TCP byte stream (Port 22):
1. **Transport Layer:** Handles algorithm negotiation, ephemeral key exchange, symmetric session encryption (Confidentiality), message authentication codes (Integrity), and server host key verification.
2. **User Authentication Layer:** Validates client account access against the server via passwords or asymmetric cryptographic signatures.
3. **Connection Protocol Layer:** Multiplexes multiple logical channels (interactive shells, SCP/SFTP file transfers, and port forwarding) over the established encrypted tunnel.

### Dual Identity Verification
- **Server Authentication:** Prevents Man-in-the-Middle (MitM) interception by comparing the server's `/etc/ssh/ssh_host_ed25519_key.pub` SHA256 fingerprint before registering it inside the client's `~/.ssh/known_hosts` record.
- **User Authentication:** Proves account ownership using an Ed25519 key pair. The private key (`id_ed25519`) remains strictly on the client to sign challenges locally, while the public key (`id_ed25519.pub`) is appended to `~/.ssh/authorized_keys` on the remote server.

---

## 3. Laboratory Environment
| Component | Specification |
| :--- | :--- |
| **Client Platform** | Windows 10/11 Host (`OpenSSH_for_Windows`) |
| **Server Platform** | Kali Linux Virtual Machine (`openssh-server` / `sshd`) |
| **Transport & Port** | TCP Port 22 |
| **Key Algorithm** | Ed25519 (`ssh-ed25519`) |
| **Scope Boundary** | Isolated Host-to-VM laboratory network |

---

## 4. Step-by-Step Implementation

### Phase 1: Client & Server Readiness
1. **Verify Client Installation (Windows PowerShell/CMD):**
   ```powershell
   ssh -V
   ```
2. **Install and Start OpenSSH Daemon (Kali Linux Server):**
   ```bash
   sudo apt update && sudo apt install -y openssh-server
   sudo systemctl enable --now ssh
   ```
3. **Confirm Service Status and Socket Listener:**
   ```bash
   systemctl status ssh --no-pager
   sudo ss -tlnp | grep ':22'
   ```
4. **Record Target Identity Details:**
   ```bash
   whoami
   hostname
   hostname -I
   ```

### Phase 2: Server Host Fingerprint Trust & Password Login
1. **Generate Expected Host Key Fingerprint on Kali Server:**
   ```bash
   sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
   ```
2. **Initiate First SSH Connection from Windows Client:**
   ```powershell
   ssh <kali_username>@<kali_ip>
   ```
3. **Verify and Accept Host Key:**
   Match the `SHA256:...` string displayed in the Windows terminal against the Kali console output. Type `yes` to store the host identity in `C:\Users\<User>\.ssh\known_hosts`, then authenticate with the remote user password.
4. **Verify Remote Execution Context:**
   ```bash
   whoami
   hostname
   pwd
   exit
   ```

### Phase 3: Asymmetric Key Pair Generation & Deployment
1. **Generate an Ed25519 Key Pair on Windows Client:**
   ```powershell
   ssh-keygen -t ed25519 -C "student@lab"
   ```
   *(Saved to default path `$HOME\.ssh\id_ed25519`)*
2. **Inspect the Public Key Fingerprint:**
   ```powershell
   ssh-keygen -lf $HOME\.ssh\id_ed25519.pub
   ```
3. **Install Public Key onto Kali Linux Server:**
   Using PowerShell pipeline to ensure directory and file permissions (`700` for `~/.ssh` and `600` for `authorized_keys`):
   ```powershell
   type $HOME\.ssh\id_ed25519.pub | ssh <kali_username>@<kali_ip> "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
   ```

### Phase 4: Enforced Public-Key Authentication Test
1. **Connect with Password Fallback Disabled:**
   ```powershell
   ssh -o PreferredAuthentications=publickey -o PasswordAuthentication=no <kali_username>@<kali_ip>
   ```
2. **Confirm Remote Session Identity:**
   ```bash
   whoami
   hostname
   exit
   ```

---

## 5. Diagnostics & Troubleshooting Reference
| Symptom | Probable Cause | Verification / Resolution |
| :--- | :--- | :--- |
| `Connection refused` | `sshd` daemon stopped or not bound to port 22 | Run `systemctl status ssh` and `sudo ss -tlnp \| grep ':22'` |
| `Connection timed out` | Incorrect IP address, VM network mode, or firewall | Verify IP with `hostname -I` and VM adapter settings |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` | Host key regenerated or potential MitM interception | Stop connection; verify `/etc/ssh/ssh_host_ed25519_key.pub` on console |
| `Permission denied (publickey)` | Bad file permissions on server or wrong key offered | Ensure `chmod 700 ~/.ssh` and `chmod 600 ~/.ssh/authorized_keys`; trace with `ssh -vv` |

---

## 6. Submission Evidence Checklist
- [x] Windows OpenSSH client version output (`ssh -V`)
- [x] Kali `sshd` active service status and port 22 listening socket (`systemctl` & `ss`)
- [x] Out-of-band server host key SHA256 fingerprint match
- [x] Password-authenticated remote shell proof (`whoami`, `hostname`, `pwd`)
- [x] Client Ed25519 public key SHA256 fingerprint (`ssh-keygen -lf`)
- [x] Passwordless / key-only authentication verification (`PasswordAuthentication=no`)
