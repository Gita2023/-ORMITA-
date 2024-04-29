import pandas as pd

# Define the base class Company
class Company:
    def __init__(
            self, cash, account_receivables, inventory, current_assets,
            noncurrent_assets, accu_depr, intangible_assets, longterm_investments,
            current_lia, noncurrent_lia, owners_equity, net_income, ebit,
            total_rev, sales_rev, total_exp, operating_exp, interest_exp, depr_exp, wages_exp,
            date_record
    ):
        # Assigning values to attributes
        # Current Assets
        self.cash = cash
        self.account_receivables = account_receivables
        self.inventory = inventory
        self.current_assets = current_assets
        
        # Non-current assets and depreciables
        self.noncurrent_assets = noncurrent_assets
        self.accu_depr = accu_depr
        self.intangible_assets = intangible_assets
        self.longterm_investments = longterm_investments
        
        # Liabilities
        self.current_lia = current_lia
        self.noncurrent_lia = noncurrent_lia
        
        # Equity
        self.owners_equity = owners_equity
        self.net_income = net_income 
        self.ebit = ebit        
        
        # Income statement 
        self.total_rev = total_rev
        self.sales_rev = sales_rev
        self.total_exp = total_exp
        self.operating_exp = operating_exp
        self.interest_exp = interest_exp
        self.depr_exp = depr_exp
        self.wages_exp = wages_exp

        # Balance sheet date
        self.date_record = date_record
    
    # Totals Methods
    # - Total assets calculation
    def total_assets(self):
        return self.cash + self.account_receivables + self.inventory +self.noncurrent_assets + self.current_assets + self.intangible_assets + self.longterm_investments - self.accu_depr
    
    # - Total liabilities calculation
    def total_lia(self):  
        return self.current_lia + self.noncurrent_lia

    # Financial Ratios methods
    # - Liquidity ratio calculation
    # -- Current Ratio
    def current_ratio(self):
        return self.current_assets / self.current_lia
    
    # -- Quick ratio
    def quick_ratio(self):
        return (self.current_assets - self.inventory) / self.current_lia
    
    # -- Cash ratio
    def cash_ratio(self):
        return self.cash / self.current_lia
    
    # - Financial leverage
    # -- Total debt ratio
    def total_debt_ratio(self):
        return (self.total_assets() - self.owners_equity) / self.total_assets() 
    
    # -- Debt Equity ratio
    def dept_equity_ratio(self):
        return self.total_lia() / self.owners_equity
    
    # -- Equity Multiplier
    def equity_multi(self):
        return self.total_assets() / self.owners_equity
    
    # -- Times interest earned ratio
    def tie(self):
        return self.ebit / self.interest_exp
    
    # -- Cash Coverage Ratios
    def cash_cov_ratio(self):
        return (self.ebit + self.depr_exp) / self.interest_exp
    
    # - Turnover Measures
    # -- Receivables turnover
    def rece_trnovr(self):
        return self.sales_rev / self.account_receivables
    
    # -- Days’ sales in receivables
    def days_sales_rece_trnover(self):
        return 365 / self.rece_trnovr()
    
    #  -- Total asset turnover
    def total_asset_trnovr(self):
        return self.sales_rev / self.total_assets()
    
    # - Profitability Measures
    # -- Profit margin
    def profit_marg(self):
        return self.net_income / self.total_rev
    
    # -- Return on assets
    def return_assets(self):
        return self.net_income / self.total_assets()
    
    # -- Return on equity
    def return_equity(self):
        return self.net_income / self.owners_equity
    
    def wages_rev_ratio(self):
        return self.wages_exp / self.total_rev
    
    # Create DataFrame method
    def create_df(self):
        # Gathering data in a list
        list_ratios = [
            self.date_record,
            self.current_ratio(), self.quick_ratio(), self.cash_ratio(),
            self.total_debt_ratio(), self.dept_equity_ratio(), self.equity_multi(),
            self.tie(), self.cash_cov_ratio(), self.rece_trnovr(), 
            self.days_sales_rece_trnover(), self.total_asset_trnovr(),
            self.profit_marg(), self.return_assets(), self.return_equity(),
            self.wages_rev_ratio()
        ]

        # Convert to DataFrame
        df = pd.DataFrame([list_ratios], columns=[
            "Date", "Current_Ratio", "Quick_Ratio", "Cash_Ratio", 
            "Total_Debt_Ratio", "Debt_Equity_Ratio", "Equity_Multiplier", 
            "Times_Interest_Earned", "Cash_Coverage_Ratio", "Receivables_Turnover", 
            "Days_Sales_Receivables", "Total_Asset_Turnover", "Profit_Margin", 
            "Return_on_Assets", "Return_on_Equity", "Wages_to_Revenue_Ratio"
        ])

        return df

# Hotel subclass
class Hotel(Company):
    def __init__(
        self, room_num_aval, room_rev, room_num_occ, room_num_sold,
        cash, account_receivables, inventory, current_assets, noncurrent_assets, accu_depr,
        intangible_assets, longterm_investments, current_lia, noncurrent_lia,
        owners_equity, net_income, ebit, total_rev, sales_rev, total_exp,
        operating_exp, interest_exp, depr_exp, wages_exp, date_record
    ):
        # Intializing subclass attributes
        self.room_num_aval = room_num_aval
        self.room_num_occ = room_num_occ
        self.room_rev = room_rev
        self.room_num_sold = room_num_sold

        # Initialize attributes from the base class within the subclasses
        super().__init__(
            cash, account_receivables, inventory, current_assets, noncurrent_assets, accu_depr,
            intangible_assets, longterm_investments, current_lia, noncurrent_lia,
            owners_equity, net_income, ebit, total_rev, sales_rev, total_exp,
            operating_exp, interest_exp, depr_exp, wages_exp, date_record
        )
        
    # Other metrics methods
    # - Gross operation profit calculation 
    def GOP(self):
        return self.total_rev - self.operating_exp
    
    # - Occupation rate
    def occ_rate(self):
        return self.room_num_occ / self.room_num_aval
    
    #
