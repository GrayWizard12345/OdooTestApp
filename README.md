# Education Center Payment Automation - Odoo Addon

This Odoo addon automates payments for an education center. It includes models for courses, groups, payments, students, and teachers, along with corresponding views.

## Features

- Manage courses offered by the education center.
- Organize students and teachers into groups.
- Track payments made by students.
- Maintain records of students and teachers.

## Installation

1. Clone this repository to your Odoo addons directory:

   ```bash
   git clone https://github.com/GrayWizard12345/OdooTestApp.git
   ```

2. Restart your Odoo server.

3. Install the addon from the Odoo Apps interface.

## Usage
1. Navigate to the Courses menu to manage courses.
2. Create groups in the Groups menu and assign students and teachers.
3. Track payments in the Payments menu.
4. Manage student and teacher records in the respective menus.

### Groups and Users
This addon comes with the following predefined groups and users:

#### Groups
1. educationcenter.group_administrator - full privileges
2. educationcenter.group_admin - partial privileges

Full details can be found here:
[TestOdooApp](https://ruzimurodovnodirjon.notion.site/Odoo-test-topshiriq-020d6e952ce048bebd7cb8ac307a27db)


#### Users
super_user: assigned to group_administrator.
admin: assigned to group_admin.

For both users the password is the same as login.
Details for predefined groups and users can be found at [data](src/educationcenter/data) folder.

### License
This project is licensed under the BSD License.