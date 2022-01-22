%HECHOS%
antigüedad_instalacion(10).
antigüedad_instalacion(20).
antigüedad_instalacion(30).
antigüedad_instalacion(40).
antigüedad_instalacion(50).



material_tuberia(plomo, 20).
material_tuberia(pvc, 45).
material_tuberia(cobre, 90).


dura_mas(cobre, pvc).
dura_mas(cobre, plomo).
dura_mas(pvc, plomo).

existe_desgaste(plomo, 21).
existe_desgaste(pvc, 46).
existe_desgaste(cobre, 91).

existe_desgaste_exposicion(plomo, 10).
existe_desgaste_exposicion(plomo, 20).
existe_desgaste_exposicion(plomo, 30).
existe_desgaste_exposicion(plomo, 40).
existe_desgaste_exposicion(plomo, 50).
existe_desgaste_exposicion(plomo, 60).
existe_desgaste_exposicion(plomo, 70).
existe_desgaste_exposicion(plomo, 80).
existe_desgaste_exposicion(cobre, 5).
existe_desgaste_exposicion(cobre, 10).
existe_desgaste_exposicion(cobre, 25).
existe_desgaste_exposicion(cobre, 30).
existe_desgaste_exposicion(cobre, 45).
existe_desgaste_exposicion(cobre, 50).
existe_desgaste_exposicion(cobre, 60).
existe_desgaste_exposicion(cobre, 70).
existe_desgaste_exposicion(pvc, 10).
existe_desgaste_exposicion(pvc, 23).
existe_desgaste_exposicion(pvc, 33).
existe_desgaste_exposicion(pvc, 43).
existe_desgaste_exposicion(pvc, 53).
existe_desgaste_exposicion(pvc, 63).
existe_desgaste_exposicion(pvc, 73).
existe_desgaste_exposicion(pvc, 84).

consumo_agua(alto).
consumo_agua(medio).
consumo_agua(bajo).

existe_mantenimiento(plomo).
existe_mantenimiento(cobre).

tipo_de_fuga(desapercibida).
tipo_de_fuga(humedad).
tipo_de_fuga(volumen).

presión_agua(alta).
presión_agua(media).
presión_agua(baja).

señal_fisica(olor).
señal_fisica(mancha).
señal_fisica(sonido).
señal_fisica(charco).
señal_fisica(hongos).

asentamiento_terreno("arcillas expansivas").

%REGLAS%
presion_agua(x) :- consumo_agua(x).
dura_mas(X,Y,W) :- existe_mantenimiento(X,Y),material_tuberia(X, W).

afectación(X,Y):- tipo_de_fuga(X), asentamiento_del_terreno(Y).
factores_visibles(X,Y):- tipo_de_fuga(X), señal_fisica(Y).

