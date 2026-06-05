Modelo de clasificación que identifica solicitudes de crédito de alto riesgo con AUC-ROC de 0,76.

## El problema
Los bancos en busca de mejorar la vida de las personas ofrecen productos financieros que en ocasiones resultan riesgosos para la propia entidad, como lo son los creditos. Saber si un cliente será buen pagador o incurrirá en mora es un problema del día a día, ya que tener un cliente en mora le puede costar mucho dinero al banco. Es allí donde con ayuda del analisis de datos y modelos de machine learning, se ha logrado detectar cuáles son las variables que ayudan a detectar un buen cliente y uno que no, logrando captar al menos el 65% de los clientes que pueden incurrir en mora. 

## Los datos
Para este proyecto se ha utilizado la data de HomeCredit. Tenemos información de más de 300K solicitudes de crédito que incluyen datos sobre el género, nivel de ingresos, nivel educativo, nivel de endeudamiento, antigüedad laboral, entre otras.

## Hallazgos
- Nos encontramos con una distribución entre clientes que pagan y los que incurren en impago, siendo los primeros de los que más datos se tienen. Con más de 300K solicitudes analizadas, el 8% -aproximadamente 24.000 clientes- corresponden a clientes en mora.
- Hay una clara relación entre la edad y la tasa de impago, siendo las personas más jovenes los que más incurren en esto con un 12% comparado con menos de 6% para las personas de mayor edad.
- Al analizar la correlación entre tipo de ingreso y tasa de impago encontramos que el grupo con mayor tasa de impago -40% aprox.- son las personas con baja por maternidad, seguido de los desempleados con un 35%, mientras que los estudiantes y los dueños de negocio tienen un nivel de impago de aproximadamente 0%.

## Modelo
El modelo que se ha entrenado para este proyecto busca identificar las variables de mayor peso a la hora de detectar los clientes que incurren en impago, logrando detectar hasta el 65% de estos perfiles.

El modelo encontró que las 5 variables que más importan a la hora de detectar los perfiles de impago son: las fuentes externas de scoring crediticio -de las cuales tenemos 3-, cuánto cubre el crédito del valor del bien a financiar y el género del cliente*.

*Si bien el género aparece como variable relevante, su uso en decisiones crediticias debe evaluarse bajo el marco regulatorio vigente.

## Resultados

| Modelo              | AUC-ROC |    Std   |
|---------------------|:-------:|:--------:|
| LightGBM            | 0.75887 | 0.005474 |
| Logistic Regression | 0.74751 | 0.004720 |
| Random Forest       | 0.72245 | 0.003936 |
| DummyClassifier     | 0.5     | 0.0      |


## Cómo reproducir
1. Clonar repositorio a tu entorno local.
2. Crear entorno virtual a partir de environment.yml:
   conda env create -f environment.yml
   conda activate nombre_del_entorno
3. Descargar la data de [HomeCredit](https://www.kaggle.com/c/home-credit-default-risk).
4. Agregar la data en la carpeta Data/raw -en caso de no tenerla al clonar el repositorio se debe crear-.
5. Ejecutar los Notebooks en orden.

## Limitaciones
Si bien el análisis realizado en este proyecto se pudo detectar el 65% de los impagos, existen limitaciones con respecto a la data, tales como la antigüedad de los datos, la ubicación geográfica y posibles relaciones no detectadas durante la exploración.

Se debe evaluar la posibilidad de obtener nuevos datos para tener un perfil actualizado de los clientes que ayuden al modelo a detectar impagos con datos que reflejen la realidad actual. 