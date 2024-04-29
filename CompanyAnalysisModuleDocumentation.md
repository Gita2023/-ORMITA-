## CompanyAnalyticsModule

Within this module, you'll find classes tailored for analyzing the financial data of various company types, covering a spectrum from hotels to mining/forestry companies.

### Classes

#### Company

This serves as the base class for all company types.

**Attributes**
- `cash`: Float, representing the company's cash holdings.
- `account_receivables`: Float, indicating the value of accounts receivable.
- `inventory`: Float, denoting the value of inventory.
- `current_assets`: Float, representing the value of current assets.
- `noncurrent_assets`: Float, representing the value of non-current assets.
- `accu_depr`: Float, indicating accumulated depreciation.
- `intangible_assets`: Float, representing the value of intangible assets.
- `longterm_investments`: Float, representing the value of long-term investments.
- `current_lia`: Float, indicating the value of current liabilities.
- `noncurrent_lia`: Float, indicating the value of non-current liabilities.
- `owners_equity`: Float, indicating the value of owners' equity.
- `net_income`: Float, representing the net income.
- `ebit`: Float, representing earnings before interest and taxes.
- `total_rev`: Float, representing total revenue.
- `sales_rev`: Float, representing revenue from sales.
- `total_exp`: Float, representing total expenses.
- `operating_exp`: Float, representing operating expenses.
- `interest_exp`: Float, representing interest expenses.
- `depr_exp`: Float, representing depreciation expenses.
- `wages_exp`: Float, representing wages expenses.
- `date_record`: String, representing the date of the financial record.

**Methods**
- `total_assets()`: Calculates the total assets of the company.
- `total_lia()`: Calculates the total liabilities of the company.

**Financial Ratios Methods**
- `current_ratio()`: Calculates the current ratio.
- `quick_ratio()`: Calculates the quick ratio.
- `cash_ratio()`: Calculates the cash ratio.
- `total_debt_ratio()`: Calculates the total debt ratio.
- `dept_equity_ratio()`: Calculates the debt to equity ratio.
- `equity_multi()`: Calculates the equity multiplier.
- `tie()`: Calculates the times interest earned ratio.
- `cash_cov_ratio()`: Calculates the cash coverage ratio.
- `rece_trnovr()`: Calculates the receivables turnover.
- `days_sales_rece_trnover()`: Calculates the days' sales in receivables turnover.
- `total_asset_trnovr()`: Calculates the total asset turnover.
- `profit_marg()`: Calculates the profit margin.
- `return_assets()`: Calculates the return on assets.
- `return_equity()`: Calculates the return on equity.
- `wages_rev_ratio()`: Calculates the ratio of wages expenses to total revenue.

**Additional Methods**
- `create_df()`: Generates a DataFrame containing financial ratios for the company, serving as the basis for further analysis.

#### Hotel, Trade, Agriculture, ServiceSector, Manuf, MiningForestry

**Hotel**
- This subclass of Company is specifically tailored for hotels.

**Additional Attributes**
- `room_num_aval`: Integer, representing the number of available rooms.
- `room_rev`: Float, representing the revenue generated from room sales.
- `room_num_occ`: Integer, representing the number of rooms occupied.
- `room_num_sold`: Integer, representing the number of rooms sold.

**Additional Methods**
- `GOP()`: Calculates the gross operating profit.
- `occ_rate()`: Calculates the occupancy rate.
- `ave_daily_rate()`: Calculates the average daily room rate.
- `rev_per_room_aval()`: Calculates revenue per available room.
- `GOPPAR()`: Calculates gross operating profit per available room.
- `rev_par()`: Calculates revenue per available rooms.
- `create_df()`: Generates a DataFrame containing financial ratios specific to hotels.

**Trade**
- This subclass of Company is tailored for trade companies.

**Additional Attributes**
- `cogs`: Float, representing the cost of goods sold.
- `ave_inv`: Float, representing the average inventory value.

**Additional Methods**
- `inv_trnovr()`: Calculates inventory turnover.
- `days_sales_inv_trnovr()`: Calculates days' sales in inventory turnover.
- `create_df()`: Generates a DataFrame containing financial ratios specific to trade companies.

**Agriculture**
- This subclass of Company is tailored for agriculture businesses.

**Additional Attributes**
- `total_farm_area`: Float, representing the total farm area.
- `total_farm_rev`: Float, representing the total revenue generated from farming.
- `total_num_stock`: Integer, representing the total number of livestock.
- `total_stock_rev`: Float, representing the total revenue generated from livestock.

**Additional Methods**
- `land_yield()`: Calculates the yield per unit of farm area.
- `livestock_yield()`: Calculates the yield per livestock.
- `create_df()`: Generates a DataFrame containing financial ratios specific to agriculture businesses.

**ServiceSector**
- This subclass of Company is tailored for service sector companies.

**Additional Attributes**
- `total_fee_rev`: Float, representing the total fee revenue.
- `equity_partner_num`: Integer, representing the number of equity partners.
- `consultant_num`: Integer, representing the number of consultants.

**Additional Methods**
- `profit_marg_partner()`: Calculates the profit margin per partner.
- `fee_rev_consultant_ratio()`: Calculates the fee revenue per consultant.
- `create_df()`: Generates a DataFrame containing financial ratios specific to service sector companies.

**Manuf**
- This subclass of Company is tailored for manufacturing companies.

**Additional Attributes**
- `mtrils_cost`: Float, representing the cost of materials.
- `manuf_cost`: Float, representing the manufacturing cost.

**Additional Methods**
- `inv_trnovr()`: Calculates inventory turnover.
- `manuf_cost_exp_ratio()`: Calculates the manufacturing cost to expenses ratio.
- `mtrils_cost_exp_ratio()`: Calculates the materials cost to expenses ratio.
- `create_df()`: Generates a DataFrame containing financial ratios specific to manufacturing companies.

**MiningForestry**
- This subclass of Company is tailored for mining and forestry companies.

**Additional Attributes**
- `accu_depl`: Float, representing accumulated depletion.
- `depl_exp`: Float, representing depletion expense.

**Additional Methods**
