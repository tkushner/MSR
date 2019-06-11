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