from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Campos específicos para cada variante do produto
    marca = fields.Char('Marca', help="Marca da variante do produto")
    modelo = fields.Char('Modelo', help="Modelo da variante do produto")
    serial_number = fields.Char('Número de Série', help="Número de série da variante")
    cor = fields.Char('Cor', help="Cor da variante do produto")
    acessorio = fields.Char('Acessório', help="Acessórios específicos da variante")
    defeito = fields.Text('Defeito', help="Descrição do defeito da variante")