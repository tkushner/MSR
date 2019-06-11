%Analysis of User Timeline
% time zone analysis first
clear all;
dataTable = readtable('splitTZ_06112019.csv');
%%
data = table2array(dataTable);

meanDT = mean(data(:,2:end));
stdDT = std(data(:,2:end));

display(['max TZ: ',num2str(meanDT(6)),' (', num2str(stdDT(6)),')'])
display(['mean TZ: ',num2str(meanDT(7)),' (', num2str(stdDT(7)),')'])
display(['min TZ: ',num2str(meanDT(8)),' (', num2str(stdDT(8)),')'])
display(['mode TZ: ',num2str(meanDT(9)),' (', num2str(stdDT(9)),')'])
display(['stdev TZ: ',num2str(meanDT(10)),' (', num2str(stdDT(10)),')'])

%%
dataRaw = readtable('TZdata_raw.csv');
data2 = table2array(dataRaw);

%%
diffTZ = data2(:,5);
fitdist(data2(:,5),'normal')

display(['Percent in same time zone: ', num2str(sum(diffTZ == 0)/length(diffTZ))])
display(['Percent within 1hr zone: ', num2str(sum(abs(diffTZ) <= 60)/length(diffTZ))])
display(['Percent within 2hr zone: ', num2str(sum(abs(diffTZ) <= 120)/length(diffTZ))])
display(['Percent within 3hr zone: ', num2str(sum(abs(diffTZ) <= 180)/length(diffTZ))])
display(['Percent within 4hr zone: ', num2str(sum(abs(diffTZ) <= 240)/length(diffTZ))])
display(['Percent within 5hr zone: ', num2str(sum(abs(diffTZ) <= 300)/length(diffTZ))])
display(['Percent over 10hr zone: ', num2str(sum(abs(diffTZ) >= 600)/length(diffTZ))])





