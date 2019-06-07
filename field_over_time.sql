-- pull a field over time, sum by day, see what the values are

SELECT NewMood as NewMood_dailyMean,
    CONVERT(date,CreatedOn) as _date,
    --LEFT(CreatedOn, 11) as _date, 
    COUNT(NewMood) as NumPosts
FROM [Talklife_Data].[dbo].[Talklife_Question]
GROUP BY CONVERT(date,CreatedOn), NewMood
ORDER BY CONVERT(date,CreatedOn) ASC;