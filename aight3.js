function logDailyInflowsAndOutflows() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var transactionsSheet = ss.getSheetByName('Projection 1'); // Change to your sheet name
  var lastRow = transactionsSheet.getLastRow();
  var transactionsData = transactionsSheet.getRange(2, 1, lastRow - 1, 10).getValues(); // Assuming data starts from row 2 and there are 10 columns

  var dailyInflows = {};
  var dailyOutflows = {};

  for (var i = 0; i < transactionsData.length; i++) {
    var transaction = transactionsData[i];
    var date = transaction[6]; // Assuming 'Date' is in the 7th column (index 6)
    var value = transaction[9]; // Assuming 'Value' is in the 10th column (index 9)

    if (!date || isNaN(value)) {
      continue; // Skip rows with missing or invalid data
    }

    date = Utilities.formatDate(new Date(date), "GMT", "MM/dd/yyyy"); // Format date

    if (!dailyInflows[date]) {
      dailyInflows[date] = 0;
    }
    if (!dailyOutflows[date]) {
      dailyOutflows[date] = 0;
    }

    if (value > 0) {
      dailyInflows[date] += value;
    } else {
      dailyOutflows[date] -= value; // Convert outflows to positive values
    }
  }

  // Log the daily inflows and outflows
  for (var date in dailyInflows) {
    Logger.log("Date: " + date + ", Inflows: " + dailyInflows[date] + ", Outflows: " + dailyOutflows[date]);
  }
}

