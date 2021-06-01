# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource


class HREmployeeProfile(models.Model):
    _name = 'hr.employee.profile'
    _description = "Employee Profile"

    @api.model
    def _default_image(self):
        image_path = get_module_resource(
            'hr_employees', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())
    # last name
    last_name = fields.Char(string='Họ & Tên Lót(*):', required=False)
    # first name
    first_name = fields.Char(string='Tên(*):', required=False)
    # date of birth
    dob = fields.Date(string='Ngày sinh(*):', required=False)
    # date of joined
    doj = fields.Date(string='Ngày gia nhập:', required=False)
    # profile viewing date
    pwd = fields.Date(string='Ngày xem hồ sơ:')

    # image employee
    image_1920 = fields.Image(default=_default_image)
    # load images
    employee_images = fields.Binary(
        string="Hình Nhân Viên:", attachment=True, help="Employee Image")
    # gender
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], groups="hr.group_hr_user", tracking=True, string='Giới tính:', default='male')
    # marial
    marital = fields.Selection([
        ('single', 'Độc Thân'),
        ('married', 'Có Gia Đình'),
        ('divorced', 'Ly Hôn')
        # ('cohabitant', 'Legal Cohabitant'),
        # ('widower', 'Widower'),
    ], string='Hôn Nhân:', groups="hr.group_hr_user", default='single', tracking=True)
    #### company information ####
    ac_code = fields.Integer(string='Mã AC(*):', default=69998)
    employee_code = fields.Integer(string='Mã Nhân Viên(*):', default=70000)
    # hợp đồng lao động
    labor_contract = fields.Binary(string='Loại HĐLĐ:')
    # department code
    department_code = fields.Char(string='Mã Phòng Ban(*):', default='E04')
    # department name
    department_name = fields.Char(
        string='Tên Phòng Ban(*):', default='Hồ Tùng Mậu')
    # position code
    position_code = fields.Char(string='Mã Chức Vụ(*):', default='NVVP')
    # position name
    position_name = fields.Char(string='Tên Chức Vụ:')
    # title code
    title_code = fields.Char(string='Mã Chức Danh:')
    # title name
    title_name = fields.Char(string='Tên Chức Danh:')
    # pay rate (bậc lương)
    pay_rate = fields.Char(string='Bậc Lương:')
    # pay rate money
    pay_rate_money = fields.Float(string='Tiền Bậc:')
    # pay rate coefficient
    coeff_rate = fields.Float(string='Hệ Số Bậc:')
    # salary (tiền lương )
    salary = fields.Float(string='Tiền Lương:')
    # advance money
    advance_money = fields.Float(string='Tiền Tạm Ứng:')
    # Fringe benefits1 (phụ cấp)
    fringe_benefits1 = fields.Float(string='Phụ Cấp 1:')
    # Fringe benefits2 (phụ cấp)
    fringe_benefits2 = fields.Float(string='Phụ Cấp 2:')
    # Fringe benefits3 (phụ cấp)
    fringe_benefits3 = fields.Float(string='Phụ Cấp 3:')
    # glone(ngạch lương)
    glone = fields.Char(string='Ngạch Lương:')
    # glone money
    glone_money = fields.Float(string='Tiền Ngạch:')
    # glone coefficient
    glone_coeff = fields.Float(string='Hệ Số Ngạch:')
    # Trade union fees
    trade_union_fees = fields.Float(string='Phí Công Đoàn:')
    # social insurance
    social_insurance = fields.Float(string='Hs BHXH:')
    # social insurance 1
    social_insurance = fields.Float(string='Hs Khác 1:')
    # social insurance 2
    social_insurance = fields.Float(string='Hs Khác 2:')
    # social insurance code
    social_insurance_code = fields.Float(string='Mã Sổ BHXH:')
    # Health Insurance card code
    health_insurance_card_code = fields.Float(string='Mã Thẻ BHYT:')
    # bank card code
    bank_card_code = fields.Integer(string='Mã Thẻ NH:')
    bank_system = fields.Char(string='Hệ Thống NH:')
    bank_name = fields.Char(string='Tên Ngân Hàng:')
    # internal number
    internal_number = fields.Integer(string='Số Nội Bộ:')
    # gross /net
    gross_net = fields.Selection([
        ('gross', 'Gross'),
        ('net', 'Net')
    ], tracking=True, string='Gross/Net:', default='gross')
    # check entry card (kiem the vao)
    check_entry_card = fields.Selection([
        ('check_entry', 'Kiểm Vào'),
        ('free', 'Miễn')
    ], tracking=True, string='Kiểm Thẻ Vào:', default='check_entry')
    # check out card(Kiem the ra)
    check_out_card = fields.Selection([
        ('check_out', 'Kiểm Ra'),
        ('free', 'Miễn')
    ], tracking=True, string='Kiểm Thẻ Ra:', default='check_out')
    # tax code
    tax_code = fields.Integer(string='Mã Số Thuế:')
    # union
    union = check_out_card = fields.Selection([
        ('yes', 'Có'),
        ('no', 'Không')
    ], tracking=True, string='Công Đoàn:', default='yes')
    # login permission
    login_permission = fields.Char(string='Quyền Login:')
    ### information prersional ###
    # phone number 
    phone_numbers = fields.Integer(string='Số điện thoại:')
    # email 
    email = fields.Ch
