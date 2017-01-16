for i in {5..45}; # liczba wezlow
do
    #python generators.py -n 50 -f "data/cutMatrix$i"
    python generators.py -n $i -f "data/cutMatrix$i"
done
