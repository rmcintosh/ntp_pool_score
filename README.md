# ntp_pool_score

**ntp_pool_score** is an interface for retrieving a server's NTP pool score via [ntppool.org](https://www.ntppool.org/en/). You can import it or call it directly on the command line. It requires a Python version of at least 3.8.0.

### Examples

```python
import ntp_pool_score

score = ntp_pool_score.get_server_ntp_pool_score("127.0.0.1")

print(score)
# 20
```

```sh
python -m ntp_pool_score 127.0.0.1
# 20
```

### Installation

The easiest way to install ntp_pool_score is via pip.

```sh
pip install ntp_pool_score
```
