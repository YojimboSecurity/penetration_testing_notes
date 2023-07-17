## Technical Findings and Recommendations

In this section, we present the detailed technical findings from the penetration testing engagement. Each finding is summarized, including the description, implications, and recommendations for remediation.

| REF | RISK | ISSUE DESCRIPTION AND IMPLICATIONS | RECOMMENDATIONS |
| --- | ---- | --------------------------------- | --------------- |
| 1   | H    | Account, Password, and Privilege Management is inadequate. | All accounts should have strong passwords enforced by a strict policy. Accounts with weak passwords should be forced to change them. Accounts no longer required should be removed. |
| 2   | H    | Information enumerated through an anonymous SMB session. | Restrict access to TCP ports 139 and 445 based on roles and requirements. Disable enumeration of SAM accounts through Local Security Policy settings. |
| 3   | M    | Malicious JavaScript code can be run to silently carry out malicious activity. | Treat all user input as potentially tainted, perform proper sanitization, and encode user-controlled output when rendering pages. Do not include user input in error messages. |

For a detailed description of each finding, refer to the appendices as indicated.
