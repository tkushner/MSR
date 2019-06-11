-- pull difference matched posts & replies with local time not null
SELECT
ans.Content AS Ans,
qs.Content AS OrigQ,
ans.QuestionId AS AnsID,
qs.Id AS QiD,
qs.CreatedBy as QCreated,
ans.CreatedBy as ACreated,
ans.CreatedOn as ACreatedOn,
ans.LocalTime as ALocalTime,
qs.CreatedOn as QCreatedOn,
qs.LocalTime as QLocalTime,
DATEDIFF(mi , qs.LocalTime , ans.LocalTime ) as TDiff
FROM [Talklife_Data].[dbo].[Talklife_Answer] as ans
INNER JOIN [Talklife_Data].[dbo].[Talklife_Question] as qs
ON ans.QuestionId = qs.Id
WHERE ans.LocalTime IS NOT NULL
AND qs.LocalTime IS NOT NULL              
AND qs.IsDeleted = 0 AND ans.IsDeleted = 0
ORDER BY ans.QuestionId ASC;
