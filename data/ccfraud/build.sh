
head -n 1 transactions.csv > transactions_fraud.csv
grep -e ',1$' transactions.csv >> transactions_fraud.csv

head -n 1 transactions.csv > transactions_nonfraud.csv
grep -e ',0$' transactions.csv >> transactions_nonfraud.csv
