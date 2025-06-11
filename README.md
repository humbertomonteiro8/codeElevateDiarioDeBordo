# codeElevateDiarioDeBordo

📊 info_transportes - Análise de uso de aplicativo de transporte privado
Este projeto visa a análise de dados de corridas realizadas por meio de um aplicativo de transporte privado, com o objetivo de compreender padrões de uso pelos clientes. A partir do arquivo info_transportes.csv, geramos uma nova tabela chamada info_corridas_do_dia, com informações agregadas por data de início de corrida.

📅 Dados de entrada
O conjunto original inclui as seguintes colunas:

DATA_INICIO e DATA_FIM (formato: mm-dd-yyyy HH)

CATEGORIA (Negócio ou Pessoal)

LOCAL_INICIO e LOCAL_FIM

PROPOSITO (Ex: Reunião, Cliente, etc.)

DISTANCIA (km)

🛠️ Transformações realizadas
Os dados são processados para gerar a tabela info_corridas_do_dia, agrupada pela data de início da corrida no formato yyyy-MM-dd, contendo:

Coluna	Descrição
DT_REFE	Data de referência (yyyy-MM-dd)
QT_CORR	Total de corridas no dia
QT_CORR_NEG	Corridas da categoria “Negócio”
QT_CORR_PESS	Corridas da categoria “Pessoal”
VL_MAX_DIST	Maior distância percorrida no dia
VL_MIN_DIST	Menor distância percorrida no dia
VL_AVG_DIST	Média das distâncias percorridas
QT_CORR_REUNI	Corridas com propósito "Reunião"
QT_CORR_NAO_REUNI	Corridas com propósito definido diferente de "Reunião"
📈 Objetivo
A análise tem como foco oferecer insights sobre como os clientes utilizam o serviço, diferenciando perfis de uso pessoal e profissional, além de mapear a natureza das viagens com base nos propósitos informados.