<h2><b>Bhedak</b></h2>

---

A replacement of [`qsreplace`](https://github.com/tomnomnom/qsreplace), accepts URLs as standard input, replaces all query string values with user-supplied values and stdout. Only for `linux`, `unix` and `debian` based systems.<br/>

<h3><b>Installation</b></h3><br/>

```css
$root:~ sudo apt install python3 python3-pip
$root:~ wget https://raw.githubusercontent.com/ROX4R/bhedak/main/bhedak && chmod +x bhedak && mv bhedak /usr/bin/
```

<h3><b>Usage</b></h3><br/>

- **Example input file**
    
    ```bash
    $ waybackurls subdomain.target.tld | tee -a urls

    http://subdomain.target.tld/comment.php?pid=username&user=1
    http://subdomain.target.tld/disclaimer.php=1
    http://subdomain.target.tld/hpp/index.php?pp=12
    http://subdomain.target.tld/hpp/?pp=12&user=5
    ```

- **Replace query string values**

    ```bash
    $ cat urls | bhedak "FUZZ"

    http://subdomain.target.tld/comment.php?pid=FUZZ&user=FUZZ
    http://subdomain.target.tld/disclaimer.php=FUZZ
    http://subdomain.target.tld/hpp/index.php?pp=FUZZ
    http://subdomain.target.tld/hpp/?pp=FUZZ&user=FUZZ
    ```

- **Replace query string with custom payloads**

    ```bash
    $ cat urls | bhedak "\"><svg/onload=alert(1)>*'/---+{{7*7}}"

    http://subdomain.target.tld/comment.php?pid=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E%2A%27%2F---%2B%7B%7B7%2A7%7D%7D&user=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E%2A%27%2F---%2B%7B%7B7%2A7%7D%7D
    http://subdomain.target.tld/disclaimer.php=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E%2A%27%2F---%2B%7B%7B7%2A7%7D%7D
    http://subdomain.target.tld/hpp/index.php?pp=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E%2A%27%2F---%2B%7B%7B7%2A7%7D%7D
    http://subdomain.target.tld/hpp/?pp=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E%2A%27%2F---%2B%7B%7B7%2A7%7D%7D&user=%22%3E%3Csvg%2Fonload%3Dalert%281%29%3E%2A%27%2F---%2B%7B%7B7%2A7%7D%7D
    ```
- **Remove duplicate urls**

    ```bash
    $ cat urls | bhedak "FUZZ" | sort -u

    http://subdomain.target.tld/comment.php?pid=FUZZ&user=FUZZ
    http://subdomain.target.tld/disclaimer.php=FUZZ
    http://subdomain.target.tld/hpp/index.php?pp=FUZZ
    http://subdomain.target.tld/hpp/?pp=FUZZ&user=FUZZ
    ```

<h3><b>Donate</b></h3>
If this tool helped you or you like my work<br/>

</br><a href="https://ko-fi.com/i/IK3K34SJSA"><img src="https://ko-fi.com/img/githubbutton_sm.svg"></a>    <a href="https://rzp.io/l/pQny7s0n"><img src=".github/support.svg" width="200"></a><br/><br/>


Thanks to [`@tomnomnom`](https://github.com/tomnomnom) for making this an amazing tool called [`qsreplace`](https://github.com/tomnomnom/qsreplace), from using [`qsreplace`](https://github.com/tomnomnom/qsreplace) I got idea to make `bhedak`
