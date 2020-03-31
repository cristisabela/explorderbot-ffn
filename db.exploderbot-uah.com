@       IN      SOA     ns1.exploderbod-uah.com. admin.exploderbot-uah.com. (
                              3         ; Serial
             604800     ; Refresh
              86400     ; Retry
            2419200     ; Expire
             604800 )   ; Negative Cache TTL

; name servers - NS records
    IN      NS      ns1.exploderbot-uah.com.

; name servers - A records
ns1.exploderbot-uah.com.          IN      A       52.14.35.182
test.exploderbot-uah.com.         IN      A       52.14.35.19
