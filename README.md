# Cyber Threat Approach:

In this repository we aim to contribute to the operotionalization of cyberspace by proposing an empirically-driven pipeline to enable
consistent measurement, identification and characterization of cyber threat dynamics amid warfare events. Specifically, we leverage Internet-wide empirical data from diverse sources, namely, (i) dark IP address spaces on the Internet to detect backscatter and scanning probes, (ii) globally distributed User Datagram Protocol (UDP) sensors to quantify reflective amplification attempts, and (iii) route collectors to ingest Border Gateway Protocol (BGP) routing data. Considering the ongoing 2022 Russo-Ukrainian conflict, we perceive an opportunity to demonstrate the capability of our proposed model.

This repository is devoted to provide experimental setup and parameters that we developed and used to conduct a 7-month measurements pertained to the 2022 Russo-Ukrainian conflict.

You will find in this repository the following:

> Darknet Analysis: Merit ORION Network Telescope; SQL query to extract darknet events (scanning probes and backscatter events) pertained to Russia and Ukraine.

> Sensor Analysis: Hopscotch Sensor; data analysis scripts.

> BGP Analysis: PyBGPStream; python script to collect BGP updates associated with the RTBH technique.
