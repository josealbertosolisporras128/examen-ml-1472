# Reporte de Análisis de Datos - Pandas

`jose solis Machine Learning pandas, NC 1472`

## 1. DataFrame Convertido
```text
       Panaderia  Variedades  Kg_pan_dia
0      La Espiga          45         200
1      El Trigal          30         150
2        Don Pan          50         250
3       Casa Pan          35         180
4   Trigo Dorado          40         220
5  Pan Artesanal          25         120
```

## 2.1 Primeras Filas (head)
```text
   Panaderia  Variedades  Kg_pan_dia
0  La Espiga          45         200
1  El Trigal          30         150
```

## 2.2 Últimas Filas (tail)
```text
       Panaderia  Variedades  Kg_pan_dia
4   Trigo Dorado          40         220
5  Pan Artesanal          25         120
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Panaderia       str
Variedades    int64
Kg_pan_dia    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Panaderia   6 non-null      str  
 1   Variedades  6 non-null      int64
 2   Kg_pan_dia  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Kg_pan_dia'
```text
count      6.000000
mean     186.666667
std       47.187569
min      120.000000
25%      157.500000
50%      190.000000
75%      215.000000
max      250.000000
Name: Kg_pan_dia, dtype: float64
```

## 4. Ordenar Ascendente por Kg_pan_dia
```text
       Panaderia  Variedades  Kg_pan_dia
5  Pan Artesanal          25         120
1      El Trigal          30         150
3       Casa Pan          35         180
0      La Espiga          45         200
4   Trigo Dorado          40         220
2        Don Pan          50         250
```

## 5. Ordenar Descendente por Variedades
```text
       Panaderia  Variedades  Kg_pan_dia
2        Don Pan          50         250
0      La Espiga          45         200
4   Trigo Dorado          40         220
3       Casa Pan          35         180
1      El Trigal          30         150
5  Pan Artesanal          25         120
```

`jose solis Machine Learning pandas, NC 1472`