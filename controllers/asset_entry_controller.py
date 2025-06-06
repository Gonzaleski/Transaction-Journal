from PyQt5.QtCore import QObject, pyqtSignal
from models.asset import Asset
from controllers.transaction_entry_controller import TransactionEntryController

class AssetEntryController(QObject):
    assetAdded = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.view.add_button.clicked.connect(self.add_asset)

    def add_asset(self):
        symbol = self.view.symbol_input.text().strip().upper()
        data_source = self.view.data_source_input.text().strip()
        source_symbol = self.view.source_symbol_input.text().strip()

        if not symbol:
            self.view.status_label.setText("❌ Symbol is required.")
            return

        try:
            asset = Asset(symbol, data_source, source_symbol)
            asset.save()
            self.view.status_label.setText("✅ Asset added successfully.")
            self.view.clear_inputs()
            self.assetAdded.emit()  # Emit signal to update other views
        except Exception as e:
            self.view.status_label.setText(f"❌ Error: {str(e)}")
