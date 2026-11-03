# Experiment 7: WPA2 Four-Way Handshake Analysis Using Wireshark

## Aim
To capture and analyze the WPA2 four-way EAPOL handshake using Wireshark and identify the key information exchanged between an access point and a wireless client.

## Tools Used
- Wireshark
- Provided PCAP capture: `Network_Join_Nokia_Mobile.pcap`

## Theory
WPA2 uses a four-way EAPOL-Key handshake to establish session keys between the access point and client. The exchange uses nonces, replay counters, and MICs for secure key establishment.

## Methodology

1. Open `Network_Join_Nokia_Mobile.pcap` in Wireshark.
2. Apply the display filter:
   ```text
   eapol
   ```
3. Identify the four EAPOL-Key messages.
4. Select the following valid frames:
   - Message 1: Frame 726
   - Message 2: Frame 728
   - Message 3: Frame 733
   - Message 4: Frame 738
5. Expand **802.1X Authentication → Key Descriptor** for each frame.
6. Observe Key Information, Replay Counter, Nonce, and MIC.
7. Compare the direction and parameters of the four messages.
8. Verify completion of the four-way handshake.

## Four-Way Handshake Flow

```text
        Access Point                     Client
          Siemens                         Nokia
             |                              |
             |------ Message 1 ------------>|
             |       ANonce                 |
             |       Replay Counter: 0      |
             |                              |
             |<----- Message 2 -------------|
             |       SNonce + MIC           |
             |       Replay Counter: 0      |
             |                              |
             |------ Message 3 ------------>|
             |       ANonce + MIC           |
             |       Replay Counter: 1      |
             |                              |
             |<----- Message 4 -------------|
             |       MIC                    |
             |       Replay Counter: 1      |
             |                              |
             +------ Handshake Complete ----+
```

## Results

| Message | Frame | Direction | Replay Counter | Nonce | MIC |
|---|---:|---|---:|---|---|
| 1 of 4 | 726 | Siemens → Nokia | 0 | ANonce | Zero |
| 2 of 4 | 728 | Nokia → Siemens | 0 | SNonce | Present |
| 3 of 4 | 733 | Siemens → Nokia | 1 | ANonce | Present |
| 4 of 4 | 738 | Nokia → Siemens | 1 | Zeroed | Present |

The WPA Information Element in Frame 728 showed TKIP as the multicast and unicast cipher suite and PSK as the authentication/key-management method.

## Discussion
The PCAP contained all four EAPOL-Key messages of the WPA2 four-way handshake. The exchange demonstrated the use of ANonce, SNonce, MIC, and replay counters during key establishment.

## Output
The WPA2 four-way handshake was successfully identified and analyzed in Wireshark from the provided PCAP capture.

## Screenshots
1. Wireshark `eapol` filter showing the four handshake messages.
2. Frame 726: Message 1 of 4.
3. Frame 728: Message 2 of 4.
4. Frame 733: Message 3 of 4.
5. Frame 738: Message 4 of 4.
