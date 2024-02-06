function setColumnFormats() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName("Balance History"); // Target sheet by name
  
  // Check if the sheet exists
  if (!sheet) {
    Logger.log("Sheet named 'Balance History' not found.");
    return;
  }
  
  // Set date format for Column B
  var columnB = sheet.getRange("B:B");
  columnB.setNumberFormat("MM/dd/yyyy"); // Adjust date format as needed
  
  // Set time format for Column C
  var columnC = sheet.getRange("C:C");
  columnC.setNumberFormat("HH:mm:ss"); // Adjust time format as needed
  
  // Set dollar format for Column H
  var columnH = sheet.getRange("H:H");
  columnH.setNumberFormat("$#,##0.00"); // Adjust currency format as needed
}
