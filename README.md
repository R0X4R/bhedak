<h1 align="center"><b>Bhedak</b></h2>

A replacement of [`qsreplace`](https://github.com/tomnomnom/qsreplace), accepts URLs as standard input, replaces all query string values with user-supplied values and stdout. Only for `linux`, `unix` and `debian` based systems.<br/>

<h3><b>Installation</b></h3><br/>

```bash
$ sudo apt install python3 python3-pip
$ wget https://raw.githubusercontent.com/R0X4R/bhedak/main/bhedak && chmod +x bhedak && mv bhedak /usr/bin/
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
- **Comparsion**

    Some parsing errors
    
    ```bash
    $ cat test | qsreplace "FUZZ" | grep "failed"
    failed to parse url http://testphp.vulnweb.com/hpp/params.php?p=CWS000x%EF%BF%BD=%EF%BF%BD1N%EF%BF%BD@E%DF%AE%EF%BF%B)%EF%BF%BD@%EF%BF%BD            %EF%BF%BDHiP"D%EF%BF%BDF%EF%BF%BD
                                                                G&9%8E7%EF%BF%BD%DC%82%EF%BF%BDX;!S%EF%BF%BD%EF%BF%BD%CC%9B%EF%BF%BD%EF%BF%BD%EF%BF%BD7Jq%EF%BF%BD%EF%BF%BD%EF%BF%BD.%EF%BF%BD>%EF%BF%BDp%EF%BF%BDc%EF%BF%BDl%EF%BF%BDzG%EF%    BF%BD%DC%BEM%EF%BF%BDdkj%EF%BF%BD,%EF%BF%BD(%EF%BF%BD%EF%BF%BDT%EF%BF%BDJj)%EF%BF%BD"%EF%BF%BDT7$%EF%BF%BDH%EF%BF%BDD6)%EF%BF%BD
            x)%EF%BF%BD%D8%92%EF%BF%BD\C%EF%BF%BD|%EF%BF%BDQ%EF%BF%BDNc%EF%BF%BDb%EF%BF%BD%EF%BF%BD%EF%BF%BD b_&%EF%BF%BD5 h%EF%BF%BD%EF%BF%BDg%EF%BF%BD     ]s%EF%BF%BD0Q%EF%BF%BDL<%EF%BF%BD6%EF%BF%BDL%EF%BF%BD_%EF%BF%BDw~%EF%BF%BD[%EF%BF%BD/[%EF%BF%BDm{%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD:n-   %EF%BF%BD%EF%BF%BD%EF%BF%BD.%EF%BF%BDd1d%EF%BF%BD%EF%BF%BD?6%EF%BF%BD0    &pp=12 [parse "http://testphp.vulnweb.com/hpp/params.php? p=CWS\a\x0e000x%EF%BF%BD=%EF%BF%BD1N%EF%BF%BD@\x10E%DF%AE%EF%BF%BDI\b)%EF%BF%BD@\x1d%EF%BF%BD\x05    \x11%EF%BF%BDHiP\"\x05D%EF%BF%BDF%EF%BF%BD\vG&\x1b%D9%8E\x117%EF%BF%BD%DC%82%EF%BF%BD\x1br\x04X;!S%EF%BF%BD%EF%BF%BD%CC%9B%EF%BF%BD%EF%BF%BD%EF%BF%BD7Jq%EF%BF%BD\u007f%EF%BF%BD%EF%BF%BD.%EF%BF%BD\x01>%EF%BF%BD\x18p%EF%BF%BDc%EF%BF%BDl%EF%BF%BDzG%EF%BF%BD%DC%BEM%EF%BF%BDdkj\x1e%EF%BF%BD,%EF%BF%BD(%EF%BF%BD%EF%BF%BDT%EF%BF%BDJj)%EF%BF%BD\"%EF%BF%BDT7$%EF%BF%BDH%EF%BF%BDD6)%EF%BF%BD\vx)%EF%BF%BD%D8%92%EF%BF%BD\x1f\\\aC%EF%BF%BD|%EF%BF%BDQ%EF%BF%BDNc%EF%BF%BDb%EF%BF%BD%EF%BF%BD%EF%BF%BD b_&\x1c%EF%BF%BD5 h%EF%BF%BD%EF%BF%BDg\x0f\x14%EF%BF%BD    ]s%EF%BF%BD0Q%EF%BF%BDL<%EF%BF%BD6%EF%BF%BDL%EF%BF%BD_%EF%BF%BDw~%EF%BF%BD[\x17%EF%BF%BD/[%EF%BF%BDm{%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD:n-    %EF%BF%BD%EF%BF%BD%EF%BF%BD.%EF%BF%BDd1d%EF%BF%BD%EF%BF%BD?6%EF%BF%BD0    &pp=12": net/url: invalid control character in URL]
            
    failed to parse url http://testphp.vulnweb.com:80/guestbook.php'%22()&%1%3CScRiPt%20%3Eprompt(940521)%3C/ScRiPt%3E [parse   "http://testphp.vulnweb.com:80/guestbook.php'%22()&%1%3CScRiPt%20%3Eprompt(940521)%3C/ScRiPt%3E": invalid URL escape "%1%"]
    
    $ cat test | bhedak "FUZZ" | grep "params.php"
    http://testphp.vulnweb.com/hpp/params.php?p=FUZZ&9%8E7%EF%BF%BD%DC%82%EF%BF%BDX;!S%EF%BF%BD%EF%BF%BD%CC%9B%EF%BF%BD%EF%BF%BD%EF%BF%BD7Jq%EF%BF%BD%EF%BF%BD%EF%BF%BD.%EF%BF%BD>%EF%BF%BDp%EF%BF%BDc%EF%BF%BDl%EF%BF%BDzG%EF%BF%BD%DC%BEM%EF%BF%BDdkj%EF%BF%BD,%EF%BF%BD(%EF%BF%BD%EF%BF%BDT%EF%BF%BDJj)%EF%BF%BD"%EF%BF%BDT7$%EF%BF%BDH%EF%BF%BDD6)%EF%BF%BD
                                                    x)%EF%BF%BD%D8%92%EF%BF%BDC%EF%BF%BD|%EF%BF%BDQ%EF%BF%BDNc%EF%BF%BDb%EF%BF%BD%EF%BF%BD%EF%BF%BD b_&%EF%BF%BD5 h%EF%BF%BD%EF%BF%BDg%EF%BF%BD ]s%EF%BF%BD0Q%EF%BF%BDL<%EF%BF%BD6%EF%BF%BDL%EF%BF%BD_%EF%BF%BDw~%EF%BF%BD[%EF%BF%BD/[%EF%BF%BDm{%EF%BF%BD%EF%BF%BD%EF%BF%BD%EF%BF%BD:n-%EF%BF%BD%EF%BF%BD%EF%BF%BD.%EF%BF%BDd1d%EF%BF%BD%EF%BF%BD?6%EF%BF%BD0    &pp=FUZZ
    ```

    <br/><img src=".github/image.jpg"><br/>


    ```bash
    $ echo "http://fakedomain.com/fakefile.jsp;jsessionid=2ed4262dbe69850d25bc7c6424ba59db?hardwareid=14&tarifid=9998" | qsreplace "FUZZ"
    http://fakedomain.com/fakefile.jsp;jsessionid=2ed4262dbe69850d25bc7c6424ba59db?hardwareid=FUZZ&tarifid=FUZZ
    
    $ echo "http://fakedomain.com/fakefile.jsp;jsessionid=2ed4262dbe69850d25bc7c6424ba59db?hardwareid=14&tarifid=9998" | bhedak "FUZZ"
    http://fakedomain.com/fakefile.jsp;jsessionid=FUZZ?hardwareid=FUZZ&tarifid=FUZZ
    ```

<h3><b>Donate</b></h3>
If this tool helped you or you like my work<br/>

</br><a href="https://rzp.io/l/pQny7s0n"><img src=".github/support.svg" width="200"></a>    <a href="https://ko-fi.com/i/IK3K34SJSA"><img src="https://ko-fi.com/img/githubbutton_sm.svg"></a><br/><br/>

---

Thanks to [`@tomnomnom`](https://github.com/tomnomnom) for making an amazing tool called [`qsreplace`](https://github.com/tomnomnom/qsreplace), from using [`qsreplace`](https://github.com/tomnomnom/qsreplace) I got idea to make [`bhedak`](https://github.com/R0X4R/bhedak)