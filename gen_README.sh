python3 request.py > tables.md
sed '/^\* for XMSS-MT/ r tables.md' README.TBC.md > README.md
rm tables.md
