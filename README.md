# Sistema de Gestão de Qualidade Industrial (Python)

Este projeto é um protótipo de automação digital desenvolvido para o setor industrial. O objetivo é otimizar o processo de inspeção de peças, eliminando falhas manuais e organizando automaticamente o fluxo de aprovação, reprovação e armazenamento em caixas.

## 🚀 Funcionalidades

O sistema oferece um menu interativo com as seguintes operações:
1. **Cadastrar nova peça:** Entrada de dados (ID, Peso, Cor, Comprimento) com validação automática.
2. **Listar peças:** Exibição detalhada de itens aprovados e reprovados.
3. **Remover peça:** Exclusão de itens do registro através do ID.
4. **Listar caixas:** Monitoramento em tempo real de quantas caixas de 10 unidades foram fechadas e quantas peças estão na caixa atual.
5. **Gerar relatório final:** Resumo estatístico da produção e motivos detalhados de reprovação.

## 📋 Critérios de Qualidade (Regras de Negócio)

Para ser **aprovada**, a peça deve cumprir simultaneamente:
- **Peso:** Entre 95g e 105g.
- **Cor:** Apenas 'azul' ou 'verde'.
- **Comprimento:** Entre 10cm e 20cm.

## 🛠️ Como rodar o programa

### Pré-requisitos
- Ter o **Python 3.x** instalado no computador. Você pode baixar em [python.org](https://www.python.org/).

### Passo a Passo
1. Faça o download ou copie o código fonte para um arquivo chamado `solucao.py`.
2. Abra o terminal (ou prompt de comando).
3. Navegue até a pasta onde o arquivo foi salvo.
4. Execute o comando:
```bash
   python solucao.py
