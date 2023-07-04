from dataclasses import dataclass

@dataclass
class page_localization:
    data_company_code: dict
    data_company_receive: dict
    data_account_bank: dict
    data_date_payment: dict
    data_payment_amount: dict
    data_check_no: dict
    data_payee_name: dict
    
    payload: dict
    invoice_no: dict
    invoice_description: dict
    amt_exclude_vat: dict
    vat_amt: dict
    amt_include_vat: dict
    wht_amt: dict
    net_amount: dict
    text: dict
    fee: dict
    
    @property
    def name(self):
        name = f""
        return name
    
    def __post_int__(self):
        self.functional = ...
        self.functional2 = ...