function month2day() {
  
  
  // Handle of current spreadsheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Handle of input sheet
  var inputSheet = ss.getSheetByName("2020");
  
  // Handle of output sheet
  var outputSheet = ss.getSheetByName("Projection 1");  
  
  // Setting value of year
  var cYear = 2023;
  
  // Creating date string
  var firstDate = 'January 1, ' + cYear.toString();
  
  // Array which will hold all dates
  var dateArray = [];
  
  // Date incrementing variable
  var loopDate = new Date(firstDate);
  
  
  // Data start row
  var startRow = 2;
  
  // Getting category data
  var categoryData =  inputSheet.getRange(startRow, 1, inputSheet.getLastRow() - startRow + 1, 6).getValues();
  
  // Getting bugetdata
  var budgetData = inputSheet.getRange(startRow, 9, inputSheet.getLastRow(), inputSheet.getLastColumn()).getValues();
  
  // Creating an array of days in a month
  var daysInMonth = [];
  
  // Counter to count days for calculating days in a month
  var dayCounter = 1;
  
  // Month of last date variable
  var mold = 0;
  
  // Creating array with all dates in current year
  while (loopDate.getFullYear()<cYear+1){
    
    // Adding current value of loopDate to array
    dateArray.push(loopDate);
    
    // Incrementing loopDate
    loopDate = new Date(loopDate.getTime() + 24*60*60*1000);
    
    if (mold == loopDate.getMonth()){
      dayCounter++;
    }else{
      daysInMonth.push(dayCounter);
      dayCounter = 1;
      mold = loopDate.getMonth();
      
    }
  }
  
  var outputArray = [];
  
  // Writing the header row
  outputArray.push(["Category",	"Group", "Type", "Subtype",	"Rollerover To", "Savings Target", "Date", "Week", "Month", "Quarter", "Value"]);
  
  for (var i=0; i<categoryData.length; i++){
    
    for (var j=0; j<dateArray.length; j++){
      var cat = categoryData[i];
      var dateToAdd = (dateArray[j].getMonth()+1) + "/" + dateArray[j].getDate() + "/" + dateArray[j].getFullYear();
      var week_ta = Math.ceil((j+1)/7);
      var month_ta = dateArray[j].getMonth() + 1;
      var quarter_ta = Math.ceil(month_ta/3);
      var value = Math.round(((budgetData[i][dateArray[j].getMonth()])/daysInMonth[dateArray[j].getMonth()])*100)/100;
      
      outputArray.push(cat.concat(dateToAdd).concat(week_ta).concat(month_ta).concat(quarter_ta).concat(value));
    }//end of j forloop
    
  }// end of i forloop
  
  outputSheet.clearContents();
  outputSheet.getRange(1,1,outputArray.length,outputArray[0].length).setValues(outputArray);
  
}


function month2day2() {
  
  
  // Handle of current spreadsheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Handle of input sheet
  var inputSheet = ss.getSheetByName("2020");
  
  // Handle of output sheet
  var outputSheet = ss.getSheetByName("Projection 2");  
  
  // Setting value of year
  var cYear = 2023;
  
  // Creating date string
  var firstDate = 'January 1, ' + cYear.toString();
  
  // Array which will hold all dates
  var dateArray = [];
  
  // Date incrementing variable
  var loopDate = new Date(firstDate);
  
  
  // Data start row
  var startRow = 2;
  
  // Getting category data
  var categoryData =  inputSheet.getRange(startRow, 1, inputSheet.getLastRow() - startRow + 1, 6).getValues();
  
  // Getting bugetdata
  var budgetData = inputSheet.getRange(startRow, 9, inputSheet.getLastRow(), inputSheet.getLastColumn()).getValues();
  
  // Creating an array of days in a month
  var daysInMonth = [];
  
  // Counter to count days for calculating days in a month
  var dayCounter = 1;
  
  // Month of last date variable
  var mold = 0;
  
  // Creating array with all dates in current year
  while (loopDate.getFullYear()<cYear+1){
    
    // Adding current value of loopDate to array
    dateArray.push(loopDate);
    
    // Incrementing loopDate
    loopDate = new Date(loopDate.getTime() + 24*60*60*1000);
    
    if (mold == loopDate.getMonth()){
      dayCounter++;
    }else{
      daysInMonth.push(dayCounter);
      dayCounter = 1;
      mold = loopDate.getMonth();
      
    }
  }
  
  var outputArray = [];
  
  // Writing the header row
  outputArray.push(["Category",	"Group", "Type", "Subtype",	"Rollerover To", "Savings Target", "Date", "Week", "Month", "Quarter", "Value"]);
  
  for (var i=0; i<categoryData.length; i++){
    
    for (var j=0; j<dateArray.length; j++){
      var cat = categoryData[i];
      var dateToAdd = (dateArray[j].getMonth()+1) + "/" + dateArray[j].getDate() + "/" + dateArray[j].getFullYear();
      var week_ta = Math.ceil((j+1)/7);
      var month_ta = dateArray[j].getMonth() + 1;
      var quarter_ta = Math.ceil(month_ta/3);
      var value = Math.round(((budgetData[i][dateArray[j].getMonth()])/daysInMonth[dateArray[j].getMonth()])*100)/100;
      
      outputArray.push(cat.concat(dateToAdd).concat(week_ta).concat(month_ta).concat(quarter_ta).concat(value));
    }//end of j forloop
    
  }// end of i forloop
  
  outputSheet.clearContents();
  outputSheet.getRange(1,1,outputArray.length,outputArray[0].length).setValues(outputArray);
  
}



function month2day3() {
  
  
  // Handle of current spreadsheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Handle of input sheet
  var inputSheet = ss.getSheetByName("2020");
  
  // Handle of output sheet
  var outputSheet = ss.getSheetByName("Projection 3");  
  
  // Setting value of year
  var cYear = 2023;
  
  // Creating date string
  var firstDate = 'January 1, ' + cYear.toString();
  
  // Array which will hold all dates
  var dateArray = [];
  
  // Date incrementing variable
  var loopDate = new Date(firstDate);
  
  
  // Data start row
  var startRow = 2;
  
  // Getting category data
  var categoryData =  inputSheet.getRange(startRow, 1, inputSheet.getLastRow() - startRow + 1, 6).getValues();
  
  // Getting bugetdata
  var budgetData = inputSheet.getRange(startRow, 9, inputSheet.getLastRow(), inputSheet.getLastColumn()).getValues();
  
  // Creating an array of days in a month
  var daysInMonth = [];
  
  // Counter to count days for calculating days in a month
  var dayCounter = 1;
  
  // Month of last date variable
  var mold = 0;
  
  // Creating array with all dates in current year
  while (loopDate.getFullYear()<cYear+1){
    
    // Adding current value of loopDate to array
    dateArray.push(loopDate);
    
    // Incrementing loopDate
    loopDate = new Date(loopDate.getTime() + 24*60*60*1000);
    
    if (mold == loopDate.getMonth()){
      dayCounter++;
    }else{
      daysInMonth.push(dayCounter);
      dayCounter = 1;
      mold = loopDate.getMonth();
      
    }
  }
  
  var outputArray = [];
  
  // Writing the header row
  outputArray.push(["Category",	"Group", "Type", "Cashflow Type",	"Rollerover To", "Savings Target", "Date", "Week", "Month", "Quarter", "Value"]);
  
  for (var i=0; i<categoryData.length; i++){
    
    for (var j=0; j<dateArray.length; j++){
      var cat = categoryData[i];
      var dateToAdd = (dateArray[j].getMonth()+1) + "/" + dateArray[j].getDate() + "/" + dateArray[j].getFullYear();
      var week_ta = Math.ceil((j+1)/7);
      var month_ta = dateArray[j].getMonth() + 1;
      var quarter_ta = Math.ceil(month_ta/3);
      var value = Math.round(((budgetData[i][dateArray[j].getMonth()])/daysInMonth[dateArray[j].getMonth()])*100)/100;
      
      outputArray.push(cat.concat(dateToAdd).concat(week_ta).concat(month_ta).concat(quarter_ta).concat(value));
    }//end of j forloop
    
  }// end of i forloop
  
  outputSheet.clearContents();
  outputSheet.getRange(1,1,outputArray.length,outputArray[0].length).setValues(outputArray);
  
}







function bonus() {
  
  // Handle of current spreadsheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  
  // Handle of input sheet
  var inputSheet = ss.getSheetByName("Bonus - Input Monthly Values");
  
  // Handle of output sheet
  var outputSheet = ss.getSheetByName("");  
  
  // Setting value of year
  var cYear = 2019;
  
  // Creating date string
  var firstDate = 'January 1, ' + cYear.toString();
  
  // Array which will hold all dates
  var dateArray = [];
  
  // Date incrementing variable
  var loopDate = new Date(firstDate);
  
  
  // Date start row
  var startRow = 2;
  
  // Getting category data
  var categoryData =  inputSheet.getRange(startRow, 1, inputSheet.getLastRow(), 3).getValues();
  
  // Getting bugetdata
  var budgetData = inputSheet.getRange(startRow, 8, inputSheet.getLastRow(), inputSheet.getLastColumn()-1).getValues();
  
  // Creating array with all dates in current year
  while (loopDate.getFullYear()<cYear+1){
    
    // Adding current value of loopDate to array
    dateArray.push(loopDate);
    
    // Incrementing loopDate
    loopDate = new Date(loopDate.getTime() + 24*60*60*1000);
    
  }
  
  var outputArray = [];
  
  // Writing the header row
  outputArray.push(["Category",	"Group", "Type", "Date", "Value"]);
  
  
  for (var i=0; i<categoryData.length; i++){
    
    for (var j=0; j<dateArray.length; j++){
      
      // The five columns to add
      var cat = categoryData[i];
      var dateToAdd = (dateArray[j].getMonth()+1) + "/" + dateArray[j].getDate() + "/" + dateArray[j].getFullYear();
      var value = budgetData[i][dateArray[j].getMonth()];
      
      // Pushing the data into the array
      outputArray.push(cat.concat(dateToAdd).concat(value));
    }//end of j forloop
    
  }// end of i forloop
  
  outputSheet.clearContent();
  outputSheet.getRange(1,1,outputArray.length,outputArray[0].length).setValues(outputArray);
  
}

function removeEmptyRows(){
  var sh = SpreadsheetApp.getActiveSheet();
  var maxRows = sh.getMaxRows(); 
  var lastRow = sh.getLastRow();
  sh.deleteRows(lastRow+1, maxRows-lastRow);
}
