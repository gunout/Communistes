import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class PCFFinanceAnalyzer:
    def __init__(self):
        self.parti = "Parti Communiste Français (PCF)"
        self.colors = ['#D50000', '#FF5252', '#FF8A80', '#C51162', '#E91E63', 
                      '#F44336', '#EF5350', '#E57373', '#D32F2F', '#B71C1C']
        
        self.start_year = 1920  # Création du PCF
        self.end_year = 2025
        self.creation_year = 1920
        self.front_populaire_year = 1936
        self.liberation_year = 1945
        self.decline_start_year = 1978
        
        # Configuration spécifique au PCF
        self.config = {
            "type": "parti_politique",
            "orientation": "gauche_communiste",
            "electorat_cible": ["ouvriers", "employes", "retraites", "banlieues", "milieux_populaires"],
            "budget_base": 12,  # millions d'euros (déclin progressif)
            "adherents_base": 80000,  # Apogée dans les années 1950
            "importance": "historique",
            "sources_financement": ["cotisations", "financement_public", "presse", "municipalites", "syndicats"]
        }
        
    def generate_financial_data(self):
        """Génère des données financières pour le PCF"""
        print(f"☭ Génération des données financières pour {self.parti}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données d'adhérents et structure
        data['Adherents'] = self._simulate_adherents(dates)
        data['Sections_Locales'] = self._simulate_sections_locales(dates)
        data['Elus_Locaux'] = self._simulate_elus_locaux(dates)
        data['Elus_Nationaux'] = self._simulate_elus_nationaux(dates)
        data['Mairies'] = self._simulate_mairies(dates)
        
        # Revenus du parti
        data['Revenus_Total'] = self._simulate_total_revenue(dates)
        data['Cotisations_Adherents'] = self._simulate_membership_fees(dates)
        data['Financement_Public'] = self._simulate_public_funding(dates)
        data['Revenus_Presse'] = self._simulate_press_revenue(dates)  # L'Humanité
        data['Revenus_Municipaux'] = self._simulate_municipal_revenue(dates)
        data['Dons_Sympathisants'] = self._simulate_sympathizer_donations(dates)
        data['Revenus_Formations'] = self._simulate_training_revenue(dates)
        
        # Dépenses du parti
        data['Depenses_Total'] = self._simulate_total_expenses(dates)
        data['Depenses_Personnel'] = self._simulate_staff_expenses(dates)
        data['Depenses_Campagnes'] = self._simulate_campaign_expenses(dates)
        data['Depenses_Communication'] = self._simulate_communication_expenses(dates)
        data['Depenses_Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Depenses_Presse'] = self._simulate_press_expenses(dates)  # Soutien à L'Humanité
        data['Depenses_Formation'] = self._simulate_training_expenses(dates)
        data['Depenses_International'] = self._simulate_international_expenses(dates)
        
        # Indicateurs financiers
        data['Taux_Execution_Budget'] = self._simulate_budget_execution_rate(dates)
        data['Ratio_Cotisations_Revenus'] = self._simulate_membership_ratio(dates)
        data['Dependance_Financement_Public'] = self._simulate_public_funding_dependency(dates)
        data['Solde_Financier'] = self._simulate_financial_balance(dates)
        data['Fonds_Propres'] = self._simulate_own_funds(dates)
        
        # Investissements stratégiques
        data['Investissement_Communication'] = self._simulate_communication_investment(dates)
        data['Investissement_Formation'] = self._simulate_training_investment(dates)
        data['Investissement_Municipal'] = self._simulate_municipal_investment(dates)
        data['Investissement_Jeunesse'] = self._simulate_youth_investment(dates)
        data['Investissement_Presse'] = self._simulate_press_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques au PCF
        self._add_party_trends(df)
        
        return df
    
    def _simulate_adherents(self, dates):
        """Simule le nombre d'adhérents"""
        base_adherents = self.config["adherents_base"]
        
        adherents = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution historique des adhérents selon les périodes politiques
            if 1920 <= year <= 1936:  # Création et montée en puissance
                growth_rate = 0.20
            elif 1936 <= year <= 1939:  # Front populaire
                growth_rate = 0.35
            elif 1939 <= year <= 1944:  # Guerre et clandestinité
                growth_rate = -0.60
            elif 1944 <= year <= 1947:  # Libération - apogée
                growth_rate = 0.50
            elif 1947 <= year <= 1956:  # Guerre froide
                growth_rate = 0.10
            elif 1956 <= year <= 1968:  # Début du déclin
                growth_rate = -0.05
            elif 1968 <= year <= 1978:  # Union de la gauche
                growth_rate = 0.08
            elif 1978 <= year <= 1990:  # Déclin accéléré
                growth_rate = -0.12
            elif 1990 <= year <= 2002:  # Chute du mur de Berlin
                growth_rate = -0.15
            elif 2002 <= year <= 2012:  # Stabilisation relative
                growth_rate = -0.03
            elif 2012 <= year <= 2022:  # Nouvelles alliances
                growth_rate = -0.08
            else:  # Période récente
                growth_rate = -0.05
                
            # Ajustement pour la longue période historique
            time_factor = min(1.0, (2025 - year) / 100)  # Réduit l'impact sur longue période
            growth = 1 + growth_rate * time_factor * (i/10)
            noise = np.random.normal(1, 0.12)
            adherents.append(base_adherents * growth * noise)
        
        return adherents
    
    def _simulate_sections_locales(self, dates):
        """Simule le nombre de sections locales"""
        base_sections = 5000  # Apogée dans les années 1950
        
        sections = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1936:
                growth_rate = 0.15
            elif year <= 1947:
                growth_rate = 0.25
            elif year <= 1968:
                growth_rate = 0.02
            elif year <= 1978:
                growth_rate = 0.05
            elif year <= 1990:
                growth_rate = -0.10
            elif year <= 2000:
                growth_rate = -0.15
            elif year <= 2010:
                growth_rate = -0.08
            else:
                growth_rate = -0.05
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/8)
            sections.append(base_sections * growth)
        
        return sections
    
    def _simulate_elus_locaux(self, dates):
        """Simule le nombre d'élus locaux"""
        base_elus = 20000  # Apogée années 1970-1980
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections municipales
            if year in [1935, 1945, 1953, 1959, 1965, 1971, 1977, 1983, 1989, 1995, 2001, 2008, 2014, 2020]:
                if year <= 1945:  # Libération
                    multiplier = 2.0
                elif year <= 1977:  # Apogée municipale
                    multiplier = 1.8
                elif year <= 1995:  # Déclin
                    multiplier = 0.8
                elif year <= 2014:  # Maintien
                    multiplier = 0.6
                else:  # Période récente
                    multiplier = 0.5
            else:
                multiplier = 1.0
                
            if year <= 1978:
                growth_rate = 0.08
            elif year <= 1990:
                growth_rate = -0.10
            elif year <= 2000:
                growth_rate = -0.12
            elif year <= 2010:
                growth_rate = -0.05
            else:
                growth_rate = -0.03
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/6)
            noise = np.random.normal(1, 0.10)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_elus_nationaux(self, dates):
        """Simule le nombre d'élus nationaux"""
        base_elus = 150  # Apogée années 1940-1950
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections législatives
            if year in [1924, 1928, 1932, 1936, 1945, 1946, 1951, 1956, 1958, 1962, 1967, 1968, 1973, 1978, 1981, 1986, 1988, 1993, 1997, 2002, 2007, 2012, 2017, 2022]:
                if year == 1936:  # Front populaire
                    multiplier = 2.5
                elif 1945 <= year <= 1956:  # Apogée
                    multiplier = 3.0
                elif 1978 <= year <= 1988:  # Déclin
                    multiplier = 0.6
                elif year == 1997:  # Gauche plurielle
                    multiplier = 1.2
                elif year == 2022:  # NUPES
                    multiplier = 1.5
                else:
                    multiplier = 1.0
            else:
                multiplier = 1.0
                
            if year <= 1956:
                growth_rate = 0.10
            elif year <= 1978:
                growth_rate = -0.05
            elif year <= 2000:
                growth_rate = -0.15
            else:
                growth_rate = -0.08
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/4)
            noise = np.random.normal(1, 0.15)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_mairies(self, dates):
        """Simule le nombre de mairies contrôlées"""
        base_mairies = 300  # Apogée années 1970-1980
        
        mairies = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1945:
                growth_rate = 0.20
            elif year <= 1977:
                growth_rate = 0.15
            elif year <= 1995:
                growth_rate = -0.10
            elif year <= 2010:
                growth_rate = -0.08
            else:
                growth_rate = -0.04
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/5)
            mairies.append(base_mairies * growth)
        
        return mairies
    
    def _simulate_total_revenue(self, dates):
        """Simule les revenus totaux"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution historique des revenus
            if 1920 <= year <= 1936:  # Croissance
                growth_rate = 0.15
            elif 1936 <= year <= 1939:  # Front populaire
                growth_rate = 0.25
            elif 1939 <= year <= 1944:  # Guerre
                growth_rate = -0.40
            elif 1944 <= year <= 1947:  # Libération
                growth_rate = 0.30
            elif 1947 <= year <= 1956:  # Guerre froide
                growth_rate = 0.08
            elif 1956 <= year <= 1978:  # Déclin progressif
                growth_rate = -0.03
            elif 1978 <= year <= 1990:  # Déclin accéléré
                growth_rate = -0.10
            elif 1990 <= year <= 2002:  # Chute du mur
                growth_rate = -0.12
            elif 2002 <= year <= 2012:  # Stabilisation
                growth_rate = -0.04
            elif 2012 <= year <= 2022:  # Nouvelles alliances
                growth_rate = -0.02
            else:  # Période récente
                growth_rate = -0.01
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/5)
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_membership_fees(self, dates):
        """Simule les cotisations des adhérents"""
        base_fees = self.config["budget_base"] * 0.40  # Très dépendant des cotisations
        
        fees = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1936:
                growth_rate = 0.18
            elif year <= 1947:
                growth_rate = 0.25
            elif year <= 1978:
                growth_rate = -0.02
            elif year <= 1990:
                growth_rate = -0.12
            elif year <= 2000:
                growth_rate = -0.15
            else:
                growth_rate = -0.08
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/6)
            noise = np.random.normal(1, 0.08)
            fees.append(base_fees * growth * noise)
        
        return fees
    
    def _simulate_public_funding(self, dates):
        """Simule le financement public"""
        base_funding = self.config["budget_base"] * 0.30
        
        funding = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Dépend des résultats électoraux
            if 1945 <= year <= 1958:  # Forte représentation
                multiplier = 1.6
            elif 1978 <= year <= 1988:  # Déclin parlementaire
                multiplier = 0.7
            elif 1997 <= year <= 2002:  # Participation gouvernementale
                multiplier = 1.3
            elif year >= 2017:  # Faible représentation
                multiplier = 0.5
            else:
                multiplier = 1.0
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + 0.01 * time_factor * (i/4)
            noise = np.random.normal(1, 0.09)
            funding.append(base_funding * growth * multiplier * noise)
        
        return funding
    
    def _simulate_press_revenue(self, dates):
        """Simule les revenus de la presse (L'Humanité)"""
        base_revenue = self.config["budget_base"] * 0.15  # Important historique
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1939:  # Apogée de L'Humanité
                growth = 1 + 0.10 * max(0, (year - 1920)/20)
            elif year <= 1944:  # Clandestinité
                growth = 0.3
            elif year <= 1970:  # Déclin progressif
                growth = 1 - 0.05 * max(0, (year - 1945)/25)
            else:  # Difficultés
                growth = 1 - 0.08 * max(0, (year - 1970)/50)
                
            noise = np.random.normal(1, 0.15)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_municipal_revenue(self, dates):
        """Simule les revenus des municipalités"""
        base_revenue = self.config["budget_base"] * 0.10
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1977:  # Apogée municipale
                growth = 1 + 0.08 * max(0, (year - 1945)/32)
            elif year <= 2000:  # Déclin
                growth = 1 - 0.06 * max(0, (year - 1977)/23)
            else:  # Maintien
                growth = 1 - 0.02 * max(0, (year - 2000)/25)
                
            noise = np.random.normal(1, 0.12)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_sympathizer_donations(self, dates):
        """Simule les dons des sympathisants"""
        base_donations = self.config["budget_base"] * 0.05
        
        donations = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1936:  # Montée en puissance
                growth_rate = 0.15
            elif year <= 1978:  # Période stable
                growth_rate = 0.03
            else:  # Déclin
                growth_rate = -0.05
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/5)
            noise = np.random.normal(1, 0.14)
            donations.append(base_donations * growth * noise)
        
        return donations
    
    def _simulate_training_revenue(self, dates):
        """Simule les revenus des formations"""
        base_revenue = self.config["budget_base"] * 0.03
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1950:  # Développement des écoles du parti
                growth = 1 + 0.04 * max(0, (year - 1950)/70)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.90
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1936, 1945, 1956, 1968, 1978, 1981, 1997, 2002, 2012, 2017, 2022]:  # Années électorales
                multiplier = 1.3
            else:
                multiplier = 1.0
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 - 0.02 * time_factor * (i/4)  # Réduction progressive
            noise = np.random.normal(1, 0.08)
            expenses.append(base_expenses * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_staff_expenses(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = self.config["budget_base"] * 0.35
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1978:  # Structure importante
                growth_rate = 0.05
            elif year <= 1990:  # Rationalisation
                growth_rate = -0.08
            elif year <= 2000:  # Réduction
                growth_rate = -0.12
            else:  # Structure minimale
                growth_rate = -0.04
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 + growth_rate * time_factor * (i/5)
            noise = np.random.normal(1, 0.06)
            expenses.append(base_staff * growth * noise)
        
        return expenses
    
    def _simulate_campaign_expenses(self, dates):
        """Simule les dépenses de campagne"""
        base_campaign = self.config["budget_base"] * 0.20
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1936, 1945, 1956, 1968, 1978, 1981, 1997, 2002, 2012, 2017, 2022]:
                if year == 1936:  # Front populaire
                    multiplier = 2.5
                elif year == 1945:  # Libération
                    multiplier = 2.2
                elif year == 1997:  # Gauche plurielle
                    multiplier = 1.8
                elif year == 2022:  # NUPES
                    multiplier = 1.6
                else:
                    multiplier = 1.5
            else:
                multiplier = 0.6
                
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 - 0.01 * time_factor * (i/3)
            noise = np.random.normal(1, 0.20)
            expenses.append(base_campaign * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_communication_expenses(self, dates):
        """Simule les dépenses de communication"""
        base_communication = self.config["budget_base"] * 0.10
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1980:  # Modernisation progressive
                growth = 1 + 0.05 * max(0, (year - 1980)/40)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.12)
            expenses.append(base_communication * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = self.config["budget_base"] * 0.15
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            time_factor = min(1.0, (2025 - year) / 100)
            growth = 1 - 0.01 * time_factor * (i/4)
            noise = np.random.normal(1, 0.05)
            expenses.append(base_operating * growth * noise)
        
        return expenses
    
    def _simulate_press_expenses(self, dates):
        """Simule les dépenses pour la presse"""
        base_press = self.config["budget_base"] * 0.08
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1970:  # Soutien important à L'Humanité
                growth = 1 + 0.04 * max(0, (year - 1920)/50)
            else:  # Réduction progressive
                growth = 1 - 0.03 * max(0, (year - 1970)/50)
                
            noise = np.random.normal(1, 0.13)
            expenses.append(base_press * growth * noise)
        
        return expenses
    
    def _simulate_training_expenses(self, dates):
        """Simule les dépenses de formation"""
        base_training = self.config["budget_base"] * 0.06
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1950:  # Écoles du parti
                growth = 1 + 0.03 * max(0, (year - 1950)/70)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.09)
            expenses.append(base_training * growth * noise)
        
        return expenses
    
    def _simulate_international_expenses(self, dates):
        """Simule les dépenses internationales"""
        base_international = self.config["budget_base"] * 0.04
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1991:  # Forte dimension internationale (Komintern, etc.)
                growth = 1 + 0.05 * max(0, (year - 1920)/71)
            else:  # Réduction après chute URSS
                growth = 1 - 0.06 * max(0, (year - 1991)/30)
                
            noise = np.random.normal(1, 0.16)
            expenses.append(base_international * growth * noise)
        
        return expenses
    
    def _simulate_budget_execution_rate(self, dates):
        """Simule le taux d'exécution du budget"""
        rates = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1945:
                base_rate = 0.75  # Gestion moins professionnelle
            elif year <= 1978:
                base_rate = 0.82
            elif year <= 2000:
                base_rate = 0.78  # Difficultés financières
            else:
                base_rate = 0.85  # Professionnalisation
                
            noise = np.random.normal(1, 0.05)
            rates.append(base_rate * noise)
        
        return rates
    
    def _simulate_membership_ratio(self, dates):
        """Simule le ratio cotisations/revenus"""
        ratios = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1956:
                base_ratio = 0.50  # Très dépendant des cotisations
            elif year <= 1978:
                base_ratio = 0.45
            elif year <= 2000:
                base_ratio = 0.38
            else:
                base_ratio = 0.32  # Diversification
                
            noise = np.random.normal(1, 0.06)
            ratios.append(base_ratio * noise)
        
        return ratios
    
    def _simulate_public_funding_dependency(self, dates):
        """Simule la dépendance au financement public"""
        dependencies = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1956:
                base_dependency = 0.20  # Peu dépendant (forte base militante)
            elif year <= 1978:
                base_dependency = 0.28
            elif year <= 2000:
                base_dependency = 0.35  # Plus dépendant
            else:
                base_dependency = 0.42  # Très dépendant
                
            noise = np.random.normal(1, 0.07)
            dependencies.append(base_dependency * noise)
        
        return dependencies
    
    def _simulate_financial_balance(self, dates):
        """Simule le solde financier"""
        balances = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1936, 1945, 1956, 1968, 1978, 1981, 1997, 2002, 2012, 2017, 2022]:
                base_balance = -0.10  # Déficits électoraux
            elif year in [1929, 1939, 1947, 1962, 1973, 1986, 1993, 2008, 2020]:
                base_balance = -0.08  # Crises
            else:
                base_balance = 0.02  # Équilibre prudent
                
            noise = np.random.normal(1, 0.12)
            balances.append(base_balance * noise)
        
        return balances
    
    def _simulate_own_funds(self, dates):
        """Simule les fonds propres"""
        base_funds = self.config["budget_base"] * 0.8
        
        funds = []
        current_funds = base_funds
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [1945, 1978, 1997]:  # Périodes fastes
                change_rate = 0.15
            elif year in [1939, 1968, 1991, 2008]:  # Crises
                change_rate = -0.20
            else:
                change_rate = 0.02
                
            current_funds *= (1 + change_rate)
            noise = np.random.normal(1, 0.10)
            funds.append(current_funds * noise)
        
        return funds
    
    def _simulate_communication_investment(self, dates):
        """Simule l'investissement en communication"""
        base_investment = self.config["budget_base"] * 0.06
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1990:
                growth = 1 + 0.07 * max(0, (year - 1990)/30)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_training_investment(self, dates):
        """Simule l'investissement en formation"""
        base_investment = self.config["budget_base"] * 0.05
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1950:
                growth = 1 + 0.04 * max(0, (year - 1950)/70)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.11)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_municipal_investment(self, dates):
        """Simule l'investissement municipal"""
        base_investment = self.config["budget_base"] * 0.07
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1977:
                growth = 1 + 0.06 * max(0, (year - 1945)/32)
            elif year <= 2000:
                growth = 1 - 0.04 * max(0, (year - 1977)/23)
            else:
                growth = 1 - 0.01 * max(0, (year - 2000)/25)
                
            noise = np.random.normal(1, 0.13)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_youth_investment(self, dates):
        """Simule l'investissement jeunesse"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 1960:
                growth = 1 + 0.05 * max(0, (year - 1960)/60)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_press_investment(self, dates):
        """Simule l'investissement dans la presse"""
        base_investment = self.config["budget_base"] * 0.05
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 1970:
                growth = 1 + 0.05 * max(0, (year - 1920)/50)
            else:
                growth = 1 - 0.03 * max(0, (year - 1970)/50)
                
            noise = np.random.normal(1, 0.16)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _add_party_trends(self, df):
        """Ajoute des tendances réalistes pour le PCF"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Création du PCF (1920)
            if year == 1920:
                df.loc[i, 'Adherents'] *= 1.5
                df.loc[i, 'Sections_Locales'] *= 2.0
            
            # Front populaire (1936)
            if year == 1936:
                df.loc[i, 'Adherents'] *= 1.8
                df.loc[i, 'Elus_Nationaux'] *= 2.5
                df.loc[i, 'Revenus_Total'] *= 1.6
            
            # Libération (1945)
            if year == 1945:
                df.loc[i, 'Adherents'] *= 2.2
                df.loc[i, 'Elus_Nationaux'] *= 3.0
                df.loc[i, 'Mairies'] *= 1.8
                df.loc[i, 'Revenus_Total'] *= 1.9
            
            # Guerre froide (1947-1956)
            if 1947 <= year <= 1956:
                df.loc[i, 'Depenses_International'] *= 1.4
                df.loc[i, 'Investissement_Presse'] *= 1.3
            
            # Mai 68
            if year == 1968:
                df.loc[i, 'Adherents'] *= 1.15
                df.loc[i, 'Investissement_Jeunesse'] *= 1.4
            
            # Programme commun (1972-1977)
            if 1972 <= year <= 1977:
                df.loc[i, 'Revenus_Total'] *= 1.2
                df.loc[i, 'Depenses_Campagnes'] *= 1.5
            
            # Défaite 1978 (tournant)
            if year == 1978:
                df.loc[i, 'Adherents'] *= 0.85
                df.loc[i, 'Revenus_Total'] *= 0.90
            
            # Chute du mur de Berlin (1989-1991)
            if 1989 <= year <= 1991:
                df.loc[i, 'Adherents'] *= 0.70
                df.loc[i, 'Revenus_Total'] *= 0.80
                df.loc[i, 'Depenses_International'] *= 0.60
            
            # Gauche plurielle (1997-2002)
            if 1997 <= year <= 2002:
                df.loc[i, 'Financement_Public'] *= 1.4
                df.loc[i, 'Revenus_Total'] *= 1.15
            
            # Crise de L'Humanité (années 2000)
            if 2000 <= year <= 2010:
                df.loc[i, 'Revenus_Presse'] *= 0.70
                df.loc[i, 'Investissement_Presse'] *= 0.80
            
            # NUPES (2022)
            if year == 2022:
                df.loc[i, 'Elus_Nationaux'] *= 2.0
                df.loc[i, 'Depenses_Campagnes'] *= 1.3
                df.loc[i, 'Revenus_Total'] *= 1.1
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances du PCF"""
        # Filtrer pour la période récente (à partir de 1945 pour plus de lisibilité)
        df_recent = df[df['Annee'] >= 1945].copy()
        
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des revenus et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df_recent, ax1)
        
        # 2. Structure des revenus
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df_recent, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df_recent, ax3)
        
        # 4. Adhérents et structure
        ax4 = plt.subplot(4, 2, 4)
        self._plot_membership_structure(df_recent, ax4)
        
        # 5. Investissements stratégiques
        ax5 = plt.subplot(4, 2, 5)
        self._plot_strategic_investments(df_recent, ax5)
        
        # 6. Indicateurs financiers
        ax6 = plt.subplot(4, 2, 6)
        self._plot_financial_indicators(df_recent, ax6)
        
        # 7. Évolution des élus
        ax7 = plt.subplot(4, 2, 7)
        self._plot_elected_officials(df_recent, ax7)
        
        # 8. Situation financière
        ax8 = plt.subplot(4, 2, 8)
        self._plot_financial_situation(df_recent, ax8)
        
        plt.suptitle(f'Analyse des Finances du {self.parti} (1945-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'PCF_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des revenus et dépenses"""
        ax.plot(df['Annee'], df['Revenus_Total'], label='Revenus Totaux', 
               linewidth=2, color='#D50000', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Total'], label='Dépenses Totales', 
               linewidth=2, color='#FF5252', alpha=0.8)
        
        ax.set_title('Évolution des Revenus et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Ajouter des annotations pour les événements clés
        key_events = {1945: 'Libération', 1956: 'Guerre froide', 1968: 'Mai 68', 
                     1978: 'Défaite', 1997: 'Gauche plurielle', 2022: 'NUPES'}
        
        for year, event in key_events.items():
            if year in df['Annee'].values:
                y_val = df[df['Annee'] == year]['Revenus_Total'].values[0]
                ax.annotate(event, (year, y_val), xytext=(10, 10), 
                           textcoords='offset points', fontsize=8, 
                           arrowprops=dict(arrowstyle='->', alpha=0.6))
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des revenus"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Cotisations_Adherents', 'Financement_Public', 'Revenus_Presse', 
                     'Revenus_Municipaux', 'Dons_Sympathisants', 'Revenus_Formations']
        colors = ['#D50000', '#FF5252', '#FF8A80', '#C51162', '#E91E63', '#F44336']
        labels = ['Cotisations', 'Financement Public', 'Presse (Humanité)', 
                 'Municipalités', 'Dons Sympathisants', 'Formations']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Revenus (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Depenses_Personnel', 'Depenses_Campagnes', 'Depenses_Communication',
                     'Depenses_Fonctionnement', 'Depenses_Presse', 'Depenses_Formation', 'Depenses_International']
        colors = ['#D50000', '#FF5252', '#FF8A80', '#C51162', '#E91E63', '#F44336', '#EF5350']
        labels = ['Personnel', 'Campagnes', 'Communication', 'Fonctionnement', 'Presse', 'Formation', 'International']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_membership_structure(self, df, ax):
        """Plot des adhérents et structure"""
        # Adhérents
        ax.bar(df['Annee'], df['Adherents']/1000, label='Adhérents (milliers)', 
              color='#D50000', alpha=0.7)
        
        ax.set_title('Adhérents et Structure Territoriale', fontsize=12, fontweight='bold')
        ax.set_ylabel('Adhérents (milliers)', color='#D50000')
        ax.tick_params(axis='y', labelcolor='#D50000')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Sections locales en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Sections_Locales']/10, label='Sections Locales (dizaines)', 
                linewidth=2, color='#FF5252')
        ax2.set_ylabel('Sections Locales (dizaines)', color='#FF5252')
        ax2.tick_params(axis='y', labelcolor='#FF5252')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    def _plot_strategic_investments(self, df, ax):
        """Plot des investissements stratégiques"""
        ax.plot(df['Annee'], df['Investissement_Communication'], label='Communication', 
               linewidth=2, color='#D50000', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Formation'], label='Formation', 
               linewidth=2, color='#FF5252', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Municipal'], label='Municipal', 
               linewidth=2, color='#FF8A80', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Presse'], label='Presse', 
               linewidth=2, color='#C51162', alpha=0.8)
        
        ax.set_title('Investissements Stratégiques (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_financial_indicators(self, df, ax):
        """Plot des indicateurs financiers"""
        # Taux d'exécution budgétaire
        ax.bar(df['Annee'], df['Taux_Execution_Budget']*100, label='Taux d\'Exécution (%)', 
              color='#D50000', alpha=0.7)
        
        ax.set_title('Indicateurs Financiers', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux d\'Exécution (%)', color='#D50000')
        ax.tick_params(axis='y', labelcolor='#D50000')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Dépendance financement public en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Dependance_Financement_Public']*100, label='Dépendance Financement Public (%)', 
                linewidth=3, color='#FF5252')
        ax2.set_ylabel('Dépendance Financement Public (%)', color='#FF5252')
        ax2.tick_params(axis='y', labelcolor='#FF5252')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    def _plot_elected_officials(self, df, ax):
        """Plot de l'évolution des élus"""
        ax.plot(df['Annee'], df['Elus_Locaux']/1000, label='Élus Locaux (milliers)', 
               linewidth=2, color='#D50000', alpha=0.8)
        
        ax.set_title('Évolution des Élus', fontsize=12, fontweight='bold')
        ax.set_ylabel('Élus Locaux (milliers)', color='#D50000')
        ax.tick_params(axis='y', labelcolor='#D50000')
        ax.grid(True, alpha=0.3)
        
        # Élus nationaux en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Elus_Nationaux'], label='Élus Nationaux', 
                linewidth=2, color='#FF5252', alpha=0.8)
        ax2.set_ylabel('Élus Nationaux', color='#FF5252')
        ax2.tick_params(axis='y', labelcolor='#FF5252')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    def _plot_financial_situation(self, df, ax):
        """Plot de la situation financière"""
        # Solde financier
        ax.bar(df['Annee'], df['Solde_Financier']*100, label='Solde Financier (% du budget)', 
              color=df['Solde_Financier'].apply(lambda x: '#4CAF50' if x > 0 else '#D50000'), alpha=0.7)
        
        ax.set_title('Situation Financière', fontsize=12, fontweight='bold')
        ax.set_ylabel('Solde Financier (% du budget)', color='#D50000')
        ax.tick_params(axis='y', labelcolor='#D50000')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Fonds propres en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Fonds_Propres'], label='Fonds Propres (M€)', 
                linewidth=3, color='#FF8A80')
        ax2.set_ylabel('Fonds Propres (M€)', color='#FF8A80')
        ax2.tick_params(axis='y', labelcolor='#FF8A80')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques pour le PCF"""
        print(f"☭ INSIGHTS ANALYTIQUES - {self.parti} ({self.start_year}-{self.end_year})")
        print("=" * 70)
        
        # Filtrer pour la période récente
        df_recent = df[df['Annee'] >= 1945]
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df_recent['Revenus_Total'].mean()
        avg_expenses = df_recent['Depenses_Total'].mean()
        avg_adherents = df_recent['Adherents'].mean()
        avg_execution = df_recent['Taux_Execution_Budget'].mean() * 100
        
        print(f"Revenus moyens annuels: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Adhérents moyens: {avg_adherents:,.0f} personnes")
        print(f"Taux d'exécution budgétaire moyen: {avg_execution:.1f}%")
        
        # 2. Évolution historique
        print("\n2. 📊 ÉVOLUTION HISTORIQUE:")
        revenue_growth = ((df_recent['Revenus_Total'].iloc[-1] / 
                          df_recent['Revenus_Total'].iloc[0]) - 1) * 100
        adherents_growth = ((df_recent['Adherents'].iloc[-1] / 
                           df_recent['Adherents'].iloc[0]) - 1) * 100
        
        print(f"Évolution des revenus (1945-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Évolution des adhérents (1945-{self.end_year}): {adherents_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        membership_share = (df_recent['Cotisations_Adherents'].mean() / df_recent['Revenus_Total'].mean()) * 100
        public_funding_share = (df_recent['Financement_Public'].mean() / df_recent['Revenus_Total'].mean()) * 100
        press_share = (df_recent['Revenus_Presse'].mean() / df_recent['Revenus_Total'].mean()) * 100
        
        print(f"Part des cotisations dans les revenus: {membership_share:.1f}%")
        print(f"Part du financement public: {public_funding_share:.1f}%")
        print(f"Part des revenus de la presse: {press_share:.1f}%")
        
        # 4. Performance et efficacité
        print("\n4. 🎯 PERFORMANCE FINANCIÈRE:")
        avg_balance = df_recent['Solde_Financier'].mean() * 100
        last_funds = df_recent['Fonds_Propres'].iloc[-1]
        dependency_public = df_recent['Dependance_Financement_Public'].iloc[-1] * 100
        
        print(f"Solde financier moyen: {avg_balance:.1f}% du budget")
        print(f"Fonds propres finaux: {last_funds:.1f} M€")
        print(f"Dépendance au financement public: {dependency_public:.1f}%")
        
        # 5. Spécificités du PCF
        print(f"\n5. 🌟 SPÉCIFICITÉS DU PCF:")
        print(f"Orientation politique: {self.config['orientation']}")
        print(f"Électorat cible: {', '.join(self.config['electorat_cible'])}")
        print(f"Sources de financement: {', '.join(self.config['sources_financement'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 1920: Création du PCF au Congrès de Tours")
        print("• 1936: Front populaire")
        print("• 1945-1947: Apogée à la Libération")
        print("• 1956-1968: Guerre froide et début du déclin")
        print("• 1972-1977: Programme commun de la gauche")
        print("• 1978: Défaite électorale (tournant)")
        print("• 1981-1984: Participation au gouvernement")
        print("• 1991: Chute de l'URSS")
        print("• 1997-2002: Gauche plurielle")
        print("• 2008-2010: Crise de L'Humanité")
        print("• 2022: Accord NUPES")
        
        # 7. Recommandations stratégiques
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Moderniser l'appareil militant")
        print("• Diversifier les sources de financement")
        print("• Renforcer l'ancrage municipal")
        print("• Développer le fundraising numérique")
        print("• Optimiser la gestion des ressources")
        print("• Investir dans la formation des jeunes cadres")
        print("• Renforcer les alliances à gauche")
        print("• Maintenir le patrimoine immobilier")

def main():
    """Fonction principale pour l'analyse du PCF"""
    print("☭ ANALYSE DES FINANCES DU PARTI COMMUNISTE FRANÇAIS (1920-2025)")
    print("=" * 60)
    
    # Initialiser l'analyseur
    analyzer = PCFFinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'PCF_financial_data_1920_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données (période récente)
    df_recent = financial_data[financial_data['Annee'] >= 2000]
    print("\n👀 Aperçu des données (2000-2025):")
    print(df_recent[['Annee', 'Adherents', 'Revenus_Total', 'Depenses_Total', 'Taux_Execution_Budget']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des finances du {analyzer.parti} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Revenus, dépenses, adhérents, élus, indicateurs financiers")

if __name__ == "__main__":
    main()