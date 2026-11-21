# idsw-voice-talk

Source ledger for site/voice-packets/ ("from air to packets and back: an IDSW talk, checked").

## Session
- IDSW 2026 official agenda, https://idsw.dev/2026/index.html (fetched 21 Nov 2026)
- Day 1, session 11, 14:55-15:25: "From Air to Packets and Back: How Voice Travels Between Devices", listed speaker Yoseph Bernandus, Software Engineer at RevComm Inc.
- Content basis: two photographed slides shared via the user's messages (overview diagram + close-up). Photos not reproduced or published.

## Claims and sources (all fetched 21 Nov 2026)
- ITU-T G.711 title "Pulse code modulation (PCM) of voice frequencies": https://www.itu.int/rec/T-REC-G.711/en
- RFC 3551: PCMA/PCMU sample-based, 8-bit samples, 8,000 Hz clock; section 4.2 default 20 ms packetization; longer-packet delay trade-off: https://www.rfc-editor.org/rfc/rfc3551.html
- RFC 3550 section 5.1: "The first twelve octets are present in every RTP packet"; 16-bit sequence number increments per packet; 32-bit timestamp = sampling instant: https://www.rfc-editor.org/rfc/rfc3550.html
- Arithmetic: 8,000 x 0.020 = 160-byte payload; 160 + 12 = 172 (slide's lower label); +8 UDP +20 IPv4 = 200 bytes on the wire; 50 packets/s.
- MEMS microphone chain (capacitive diaphragm, companion ASIC, analog vs PDM vs I2S outputs, piezoelectric alternative): https://www.allaboutcircuits.com/technical-articles/introduction-to-microelectromechanical-systems-microphone-technology/
- Opus as common modern alternative: RFC 6716, https://www.rfc-editor.org/rfc/rfc6716.html

## Notes
- Slide footnote ("illustrative G.711 path, not the exact stack every device uses") is quoted in substance; the page keeps the example-not-universal framing explicit.
- assets/voice-pipeline.svg is an original diagram based on the talk's six stages and the cited standards, not a slide reproduction.
