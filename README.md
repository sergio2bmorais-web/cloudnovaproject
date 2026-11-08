# cloudnovaproject# CloudNova — Portal Corporativo Seguro na Nuvem

Projeto académico desenvolvido por Sérgio Morais no âmbito da formação CESAE Digital.

## Objetivo

Implementar um portal corporativo no Microsoft Azure, com aplicação
em contentor, segmentação de rede, acesso privado aos dados e
automatização com GitHub Actions.

## Infraestrutura

- Rede virtual: 10.0.0.0/16
- Subnet frontend: 10.0.1.0/24
- Subnet backend: 10.0.2.0/24
- Subnet management: 10.0.3.0/24
- AzureFirewallSubnet: 10.0.4.0/26
- Azure Firewall e tabela de rotas associada ao frontend e backend.
- Máquina virtual Linux para administração.
- Azure Container Registry para armazenamento das imagens.
- Azure Container Instances na subnet frontend.
- Azure SQL Database com acesso público desativado e private endpoint.
- Blob Storage com contentor privado e service endpoint no frontend.

## Aplicação

A aplicação utiliza Python e disponibiliza:

- `/` — página inicial do portal.
- `/health` — estado da aplicação em formato JSON.

A aplicação escuta na porta 8080.

## Ficheiros

- `sergiomorais.py` — código da aplicação.
- `Dockerfile` — instruções para construir e executar a imagem.
- `.github/workflows/deploy.yml` — pipeline do GitHub Actions.

## Integração contínua

A cada push na branch main, a pipeline:

1. Obtém o código do repositório.
2. Constrói a imagem Docker.
3. Valida a sintaxe do código Python.
4. Inicia um contentor de teste.
5. Testa o endpoint /health e a página inicial.
6. Apresenta os logs e remove o contentor de teste.

Esta pipeline foi executada com sucesso no GitHub Actions.

## Segurança e testes realizados

- A aplicação no Azure Container Instances respondeu ao teste /health.
- O nome DNS do servidor SQL resolveu para o IP privado 10.0.2.4.
- Foi associado um NSG à subnet backend com regras para permitir
  TCP 1433 do frontend e negar essa porta às restantes origens.
- Foram ativadas as políticas de NSG para private endpoints.
- O teste TCP da VM de gestão ao SQL terminou por timeout,
  resultado consistente com o bloqueio pretendido.

## Trabalho pendente

- Configurar e testar as regras de saída do Azure Firewall.
- Implementar autenticação com Microsoft Entra ID,
  dependente das permissões no tenant.
- Confirmar a ligação SQL a partir do contentor frontend.
- Implementar e testar o acesso da aplicação ao SQL e ao Blob Storage.
- Configurar as credenciais da pipeline de forma segura.
- Automatizar a publicação da imagem no ACR.
- Automatizar a atualização da aplicação no Azure.

## Limitação atual

A subscrição Azure for Students encontra-se desativada devido
ao esgotamento do crédito gratuito.

A integração contínua no GitHub funciona. A publicação e a
atualização no Azure aguardam a reativação da subscrição
e a configuração das credenciais.
