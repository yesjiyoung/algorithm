SELECT 
    C.company_code,
    C.founder,
    COUNT(DISTINCT LM.lead_manager_code),
    COUNT(DISTINCT SM.senior_manager_code),
    COUNT(DISTINCT M.manager_code),
    COUNT(DISTINCT E.employee_code)
FROM Company C
    LEFT JOIN Lead_Manager LM ON C.company_code = LM.company_code
    LEFT JOIN Senior_Manager SM ON C.company_code = SM.company_code
    LEFT JOIN Manager M ON C.company_code = M.company_code
    LEFT JOIN Employee E ON C.company_code = E.company_code
GROUP BY 
    C.company_code,
    C.founder
ORDER BY C.company_code

-- count(disitinct column)이 가능하고만!