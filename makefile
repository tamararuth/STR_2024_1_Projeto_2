# Nome dos scripts Python
SCRIPT_CREATE = createTasksList.py
SCRIPT_PROJECT2 = projeto2_STR.py

# Arquivos JSON a serem deletados no clean
JSON_FILE_1 = schedulability.json
JSON_FILE_2 = tasks_list.json

# Regra principal
all: run-scripts

# Executa os scripts Python
run-create:
	python3 $(SCRIPT_CREATE)

run-projeto2:
	clear
	python3 $(SCRIPT_PROJECT2)

run-scripts:
	clear
	python3 $(SCRIPT_CREATE)
	python3 $(SCRIPT_PROJECT2)

# Deleta arquivos JSON
clean:
	@echo "Deletando arquivos JSON..."
	rm -f $(JSON_FILE_1) $(JSON_FILE_2)

help:
	clear
	@echo "#############################################################"
	@echo "run-create...: Executa o script para gerar a lista de tarefas"
	@echo "run-projeto2.: Executa o script para propor o escalonamento"
	@echo "run-scripts..: Executa ambos os scripts"
	@echo "clean........: Exclui os .json criados"
	@echo "#############################################################"
