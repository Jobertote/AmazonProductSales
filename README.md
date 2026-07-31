# AmazonProductSales

Normalizado de CSV con 40K + registros.
Construccion de funciones para poder agilizar el procedimiento.

## Analisis futuro
Answer stakeholders questions:
    
¿Cuáles son los productos más demandados según las compras del último mes?
Usaría bought_in_last_month, complementado con Rating y Number_of_reviews.
¿Los productos patrocinados tienen mejores resultados que los orgánicos?
Comparar is_sponsored contra compras recientes, calificación, reseñas y precio.
¿Qué descuentos o cupones están asociados con mayor demanda?
Analizar Current/discounted_price, Listed_price e is_couponed frente a bought_in_last_month.