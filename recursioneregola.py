def _ricorsione(self, parziale):
    
    # BLOCCO 1: AGGIORNAMENTO DEL RECORD
    # Questo cambia in base a cosa chiede la traccia (cammino più lungo, più pesante, ecc.)
    if len(parziale) > self._best_score:
        self._best_score = len(parziale)
        self._best_path = list(parziale) # list() è obbligatorio per fare la fotografia!

    # BLOCCO 2: POSIZIONE CORRENTE
    ultimo_nodo = parziale[-1]

    # BLOCCO 3: ESTRAZIONE DEI CANDIDATI
    # Grafo Orientato -> self._grafo.successors(ultimo_nodo)
    # Grafo Non Orientato -> self._grafo.neighbors(ultimo_nodo)
    candidati = self._grafo.successors(ultimo_nodo)

    # BLOCCO 4: CICLO ED ESPLORAZIONE
    for candidato in candidati:
        
        # BLOCCO 5: FILTRI (Questo è l'unico pezzo che devi inventare all'esame!)
        
        # Filtro Universale (Non passare due volte nello stesso nodo)
        if candidato not in parziale:
            
            # --- Inizio Filtro Specifico del PDF ---
            if len(parziale) == 1:
                # Caso base iniziale: non ho un passato con cui confrontarmi
                parziale.append(candidato)
                self._ricorsione(parziale)
                parziale.pop()
                
            else:
                # Caso generale: confronto il futuro con il passato
                peso_futuro = self._grafo[ultimo_nodo][candidato]['weight']
                peso_passato = self._grafo[parziale[-2]][ultimo_nodo]['weight']
                
                # LA DOMANDA DELLA TRACCIA ESAME: "I pesi sono crescenti?"
                if peso_futuro > peso_passato:
                    
                    # La trinità
                    parziale.append(candidato)
                    self._ricorsione(parziale)
                    parziale.pop()
            # --- Fine Filtro Specifico del PDF ---
