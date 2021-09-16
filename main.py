

volumen_reservorio = 4.445e8
lluvia = 5e6

reduced_lluvia = lluvia *.1


new_volume = volumen_reservorio + reduced_lluvia

new_volume_5 = new_volume * 1.05

new_reduced_volume_2 = new_volume_5 * .02

new_volumen_reservorio = new_reduced_volume_2 - 2.5e5

print(f"El volumen del reservorio es {new_volumen_reservorio} m3")

