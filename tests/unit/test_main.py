import pytest

from main import somar, dividir


def teste_somar():

    # 1 Configura
    num_a = 13
    num_b = 12
    resultado_esperado = 25

    # 2 Executa
    resultado_obtido = somar(num_a, num_b)

    # 3 Valida
    assert resultado_esperado == resultado_obtido

def teste_dividir_positivo():

    # 1 Configura
    # 1.1 Dados de Entrada
    num_a = 54
    num_b = 9

    # 1.2 Resultados Esperados
    resultado_esperado = 6


    # 2 Executa
    resultado_obtido = dividir(num_a, num_b)  # executar cálculos


    # 3 Valida
    assert resultado_obtido == resultado_esperado



def teste_dividir_negativo():
        # 1 Configura
        # 1.1 Dados de Entrada
        num_a = 54
        num_b = 0

        # 1.2 Resultados Esperados
        resultado_esperado = 'Não dividiras por zero'

        # 2 Executa
        resultado_obtido =  dividir(num_a, num_b)
        # 3 Valida
        assert resultado_obtido == resultado_esperado
# lista para uso como massa de teste
lista_de_valores = [
    (8,7,15),
    (12,13,25),
    (5,9,14),
    (8,6,14),
    (9,6,15),
    (15,23,38)
]

@pytest.mark.parametrize('num_a, num_b,resultado_esperado ',lista_de_valores) # enviando os valores
def teste_somar_leitura_de_lista(num_a,num_b,resultado_esperado): # recebendo os valores
            # 1 Configura
            # utilizamos a lista como massa de teste.

            # 2 Executa
            resultado_obtido = somar(num_a, num_b)

            # 3 Valida
            assert resultado_esperado == resultado_obtido

    # TDD = Test Driven Development

    # Desenvolvimento direcionado por testes

    # Criar todos os testes de unidade no começo...
    # Executar todos os testes pelos menos 1 vez por dia..
    # Você executa todos os testes - o que acontece?
    # Tudo Certo
    # TDD :teste de medida de progresso

    # CI Continuos Integration
    # IC Integração Continua

    # (Build)--> Suite de testes -------> (Build)
    
    # escrevi isso no github

  # eu vi que vocÊ FEZ

# novamente
