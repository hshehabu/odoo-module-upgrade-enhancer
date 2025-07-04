# Module Upgrade Enhancer

An Odoo module that enhances the module upgrade process by adding a convenient upgrade button directly to the module kanban view.

## Features

- **Upgrade Button**: Adds "Upgrade" button to module kanban cards
- **Smart Visibility**: Button only appears for installed modules
- **Auto-reload**: Automatically refreshes interface after upgrade
- **Permission Control**: Only system administrators can access

## Installation

1. **Download**: Place module in your Odoo addons directory
   ```bash
   git clone <repository-url> /path/to/odoo/addons/module_upgrade_enhancer
   ```

2. **Install**: 
   - Go to Apps → Update Apps List
   - Search for "Module Upgrade Enhancer"
   - Click "Install"

## Usage

1. Navigate to **Apps** → **Apps**
2. Switch to **Kanban View**
3. Click the **"Upgrade"** button (🔄 icon) on any installed module
4. System automatically reloads after upgrade

## Technical Details

### Dependencies
- `base`: Core Odoo functionality
- `web`: Web interface components

### File Structure
```
module_upgrade_enhancer/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── ir_module_module.py    # Extended module model
└── views/
    └── module_kanban_views.xml # Enhanced kanban view
```

### Key Components
- **Model Extension**: Overrides `_button_immediate_function` for auto-reload
- **View Enhancement**: Adds upgrade button to module kanban cards with proper permissions


## Author

**Hamza**

---

*Enhances Odoo's module management interface for easier upgrades.* 