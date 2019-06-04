-- SELECT TOP 100 CreatedOn, LocalTime 
-- FROM [Talklife_Data].[dbo].[Talklife_Answer];

SELECT TOP 5 COUNT(AnswerCount) AS Answered,
    CreatedBy, 
    COUNT(CreatedBy) AS NumQs--count takes the number of rows that match
FROM [Talklife_Data].[dbo].[Talklife_Question]
WHERE AnswerCount > 0 AND IsDeleted = 0
GROUP BY CreatedBy
ORDER BY COUNT(CreatedBy) DESC;

SELECT TOP 5 COUNT(AnswerCount) AS NotAnswered,
    CreatedBy, 
    COUNT(CreatedBy) AS NumQs--count takes the number of rows that match
FROM [Talklife_Data].[dbo].[Talklife_Question]
WHERE AnswerCount = 0 AND IsDeleted = 0
GROUP BY CreatedBy
ORDER BY COUNT(CreatedBy) DESC;


-- DECLARE @QsAnwered INTEGER;

SELECT QsAnswered = COUNT(*)
FROM [Talklife_Data].[dbo].[Talklife_Question]
WHERE CreatedBy = 24 AND AnswerCount > 0;

SELECT QsNotAnswered = COUNT(*)
FROM [Talklife_Data].[dbo].[Talklife_Question]
WHERE CreatedBy = 24 AND AnswerCount = 0;



-- select one table based on another
-- SELECT TOP 100 * FROM [Talklife_Data].[dbo].[Talklife_Question] AS Qs;
-- SELECT TOP 100 * FROM [Talklife_Data].[dbo].[Talklife_Answer] AS Ans;

SELECT TOP 5 [Talklife_Data].[dbo].[Talklife_Answer].[Content],
[Talklife_Data].[dbo].[Talklife_Answer].[CreatedBy], 
[Talklife_Data].[dbo].[Talklife_Answer].[Title],
[Talklife_Data].[dbo].[Talklife_Answer].[QuestionId]
FROM [Talklife_Data].[dbo].[Talklife_Answer]
INNER JOIN [Talklife_Data].[dbo].[Talklife_Question]
ON [Talklife_Data].[dbo].[Talklife_Answer].[QuestionId] = [Talklife_Data].[dbo].[Talklife_Question].[Id];

-- SELECT [Talklife_Data].[dbo].[Talklife_Answer].* [Talklife_Data].[dbo].[Talklife_Question].*
-- FROM [Talklife_Data].[dbo].[Talklife_Answer], [Talklife_Data].[dbo].[Talklife_Question]
--     INNER JOIN Content [Talklife_Data].[dbo].[Talklife_Answer]
--         ON [Talklife_Data].[dbo].[Talklife_Answer].[QuestionId] = [Talklife_Data].[dbo].[Talklife_Question].[Id];


-- match answers to questions
SELECT TOP 50
ans.Content AS Ans,
qs.Content AS OrigQ,
ans.QuestionId AS AnsID,
qs.Id AS QiD,
qs.CreatedBy as QCreated,
ans.CreatedBy as ACreated,
ans.CreatedOn as ACreatedOn,
ans.LocalTime as ALocalTime,
qs.CreatedOn as QCreatedOn,
qs.LocalTime as QLocalTime
FROM [Talklife_Data].[dbo].[Talklife_Answer] as ans
INNER JOIN [Talklife_Data].[dbo].[Talklife_Question] as qs
ON ans.QuestionId = qs.Id
WHERE qs.CreatedBy = 3                  -- add this line to pull only one person's timeline
AND qs.IsDeleted = 0 AND ans.IsDeleted = 0
ORDER BY ans.QuestionId ASC;
