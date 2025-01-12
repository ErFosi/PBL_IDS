import pandas as pd
import numpy as np

num_rows=1000
# Random data generation
data = {
    "ts": pd.date_range(start="2025-01-01", periods=num_rows, freq='30ms').astype(str),
    "uid": [f"C{np.random.randint(1000, 9999)}" for _ in range(num_rows)],
    "id.orig_h": [f"192.168.1.{np.random.randint(1, 255)}" for _ in range(num_rows)],
    "id.orig_p": np.random.randint(1024, 65535, num_rows),
    "id.resp_h": [f"172.16.0.{np.random.randint(1, 255)}" for _ in range(num_rows)],
    "id.resp_p": np.random.randint(20, 1024, num_rows),
    "proto": np.random.choice(["tcp", "udp", "icmp"], num_rows),
    "service": np.random.choice(["http", "dns", "ftp", "ssl", "ssh", "-"], num_rows),
    "duration": np.round(np.random.uniform(0.01, 300.0, num_rows), 2),
    "orig_bytes": np.random.randint(0, 100000, num_rows),
    "resp_bytes": np.random.randint(0, 100000, num_rows),
    "conn_state": np.random.choice(["SF", "REJ", "S0", "S1", "SH", "RSTR"], num_rows),
    "local_orig": np.random.choice(["T", "F"], num_rows),
    "local_resp": np.random.choice(["T", "F"], num_rows),
    "missed_bytes": np.random.randint(0, 100, num_rows),
    "history": np.random.choice(["Dd", "ShAD", "Hr", "Fa", "Srv"], num_rows),
    "orig_pkts": np.random.randint(1, 100, num_rows),
    "orig_ip_bytes": np.random.randint(64, 65535, num_rows),
    "resp_pkts": np.random.randint(1, 100, num_rows),
    "resp_ip_bytes": np.random.randint(64, 65535, num_rows),
}

# Create DataFrame
df = pd.DataFrame(data)
#write the csv
df.to_csv("random_dataset.csv", index=False)



# Display the dataset to the user

