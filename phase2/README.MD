# Phase 2: SIEM Attack Log Analysis & Visualization

This directory contains all artifacts and dashboard outputs for **Phase 2** of the ICS344 Course Project: ingesting and visualizing the Phase 1 attack logs in Splunk.

---

## 1. Splunk Status

Ensure Splunk Enterprise is running on Kali Linux:

```bash
$ sudo /opt/splunk/bin/splunk status
# splunkd is running (PID: 107925)
```

---

## 2. Log Files for Ingestion

Three text files generated in Phase 1 are uploaded into Splunk:

| Filename            | Description                         |
| ------------------- | ----------------------------------- |
| `phase1_banner.txt` | Custom HTTP banner grabbing script  |
| `phase1_nmap.txt`   | Nmap version scan output            |
| `phase1_nikto.txt`  | Nikto web vulnerability scan output |

Place these files into a folder on the Splunk host and use **Add Data → Upload** to ingest them into the **main** index.

---

## 3. Sample Search Queries

Validate that each source was indexed correctly.

```spl
index=main source="phase1_banner.txt"
index=main source="phase1_nmap.txt"
index=main source="phase1_nikto.txt"
```

![](screenshots/log1.png)
*Search result for `phase1_banner.txt`*
![](screenshots/log2.png)
*Search result for `phase1_nmap.txt`*
![](screenshots/log3.png)
*Search result for `phase1_nikto.txt`*

---

## 4. Dashboard Construction

We created a dashboard named **HTTP Attack Dashboard** with the following panels:

1. **Pie Charts** for each log source showing event counts:

   * `phase1_banner.txt`
   * `phase1_nikto.txt`
   * `phase1_nmap.txt`

2. **Timechart** of all events over time:

   ```spl
   index=main (source="phase1_*\.txt")
   | timechart count by source
   ```

3. **Bar Chart** comparing counts by source:

   ```spl
   index=main (source="phase1_*\.txt")
   | stats count by source
   ```

![](screenshots/dashboard.png)

---

## 5. Deliverables for Phase 2

* **Splunk Searches & Screenshots**: `log1.png`, `log2.png`, `log3.png`
* **Dashboard Screenshot**: `dashboard.png`


