for i in {0..99};
do
    python generators.py -n 100 -f "data/cutMatrix$i"
done
