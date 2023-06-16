# Importar pacotes
import pandas as pd
import plotly.express as px
import seaborn as sns

# Carregar dados
df = pd.read_csv(r"bank-full.csv", sep=";")

# Visualizar dados
df

# Informações do dataset
df.info()

# Dimensões do dataset
df.shape

# Conhecendo o dataset
df.head(10)

# Estatísticas variáveis continuas
df.describe()

# Frequência das vairáveis
df.education.value_counts()
df['education'].value_counts()

df.y.value_counts()
df.loan.value_counts()

# criar gráficos e analisando as variaveis
fig = px.histogram(df, x="education", color="y")
fig.show()

# Visualizando os gráficos
df.y.value_counts()
sns.countplot(data=df, x="y")

sns.boxplot(x=df['balance'])


fig = px.box(df, x="balance")
fig.show()



