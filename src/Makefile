antlr:
	antlr -lib ./lib/ -no-listener -visitor -Dlanguage=Python3 Kafe_Grammar.g4

clean:
	rm Kafe_GrammarLexer.py Kafe_GrammarParser.py Kafe_Grammar.tokens Kafe_GrammarVisitor.py Kafe_Grammar.interp Kafe_GrammarLexer.interp Kafe_GrammarLexer.tokens

test:
	if [ -z "$(prueba)" ]; then \
		for i in $(wildcard ../tests/*/test*.kf); do \
			python3 Kafe.py $$i; \
			echo "------------------"; \
		done; \
	else \
		for i in $(wildcard ../tests/$(prueba)/test*.kf); do \
			python3 Kafe.py $$i; \
			echo "------------------"; \
		done; \
	fi
