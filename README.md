# double url encoding xss
A simple program for double encoding xss, so you don't have to do all this in the manual OwO!!
## How to install?
```
git clone https://github.com/Diperblue/enco-double_url_xss.git
```
## How to use?
### To encode in url:
```
python3 enco-double_url_xss/ -p 'Payload_to_be_encrypted' -t o
```
### To double encode url:
```
python3 enco-double_url_xss/ -p 'Payload_to_be_encrypted' -t -d
```
### Example
```
python3 enco-double_url_xss/ -p '<script>alert(1)</script>' -t o
```
```
python3 enco-double_url_xss/ -p '<script>alert(1)</script>' -t d
```
