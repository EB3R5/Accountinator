function runManually() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var spendList = ss.getSheetByName('Spend List');
  var provision = ss.getSheetByName('Provision');
  var projection = ss.getSheetByName('Add Projection');
  
  // Get all the data from the Spend List sheet
  var spendListData = spendList.getDataRange().getValues();
  
  // Initialize an array to store the keywords
  var keywords = [];
  
  // Loop through the data starting from row 5 to find checkboxes that are checked
  for (var i = 4; i < spendListData.length; i++) {
    if (spendListData[i][0] === true) { // Assuming checkboxes are in the first column
      keywords.push(spendListData[i][1]); // Assuming the keywords are in the second column
    }
  }
  
  if (keywords.length > 0) {
    // Process each keyword and filter the data
    keywords.forEach(function(keyword) {
      var data = provision.getDataRange().getValues();
      var filteredData = data.filter(function(row) {
        // Change the column index (e.g., 2) to match the column where your keywords are located.
        return row[4] == keyword;
      });
      
      projection.getRange(projection.getLastRow() + 1, 1, filteredData.length, filteredData[0].length).setValues(filteredData);
    });
  }
}
