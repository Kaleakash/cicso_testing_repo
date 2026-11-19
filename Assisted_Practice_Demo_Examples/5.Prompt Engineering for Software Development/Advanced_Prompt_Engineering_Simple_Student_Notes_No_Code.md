# Advanced Prompt Engineering
## Simple Student Notes: Concepts, Techniques, and Examples

**Audience:** Beginners, students, and software professionals  
**Learning approach:** Understand the technique first, study the example, then practise it using an AI tool. Participants should write and test their own prompts during the session.

---

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what prompt engineering is and why it is useful.
- Write clear prompts using instruction, context, input, and output format.
- Apply zero-shot, few-shot, structured, reasoning-oriented, role-based, and context-grounded prompting.
- Prepare prompts for common software engineering activities.
- Generate sample data and RAG question-and-answer examples.
- Understand reusable prompt templates and the main LangChain prompt-template concepts.
- Evaluate, improve, compare, and maintain prompts.

---

# Part 1 — Prompt Engineering Basics

## 1. What is an LLM?

A Large Language Model (LLM) is an AI model trained using large amounts of information. It can understand and generate text, answer questions, summarize documents, classify feedback, explain concepts, and assist with software development.

An LLM does not automatically know the private details of your project or organization. If a task depends on specific project information, provide that information in the prompt.

## 2. What is a prompt?

A prompt is the instruction or information given to an AI model to obtain a response.

A prompt may contain:
- A task or question.
- Background information.
- Text or data to analyse.
- Rules and limitations.
- The expected response format.

**Simple example**

Weak prompt:

> Explain APIs.

Improved prompt:

> Explain what a REST API is to a beginner who knows basic programming. Use simple language, explain why APIs are used, and give one example from an online shopping application. Finish with a short summary.

**Why is the improved prompt better?** It tells the AI what to explain, who the explanation is for, how simple the language should be, and what example to include.

## 3. What is prompt engineering?

Prompt engineering is the process of writing, testing, and improving prompts so that an AI model produces responses that are useful for a particular task.

It is not about finding one magic sentence. It is a cycle:

1. Understand the task.
2. Write a clear prompt.
3. Give the prompt to the AI model.
4. Review the response.
5. Identify what is missing or incorrect.
6. Improve the prompt and test again.

A longer prompt is not always better. Include information that helps the model complete the task.

## 4. The four elements of a good prompt

A useful prompt can be organized into four elements.

| Element           | Meaning                                | Example       |
|------------------ |----------------------------------------|---------------|
| **Instruction**   | What should the AI do?                 | Classify customer feedback. |
| **Context**       | What background should it know?        | The feedback is about an online banking application. |
| **Input**         | What information should it work on?    | Customer comments about payments and login. |
| **Output format** | How should the response look?          | Return a table with feedback, category, and reason. |

**Complete example**

> Instruction: Classify each customer comment as Positive, Negative, Neutral, or Mixed.  
> Context: These comments are about an online banking application.  
> Input: “The payment was completed quickly.” “I cannot log in to my account.”  
> Output format: Return a table with the comment, sentiment, and a short reason. Do not add information that is not present in the comments.

## 5. Clear instructions and constraints

An instruction should explain the task clearly. Use action words such as explain, summarize, classify, compare, extract, review, generate, or recommend.

| Unclear instruction                   | Clear instruction         |
|-------------------------------------- |----------------------     |
| Check this application.               | Review the application requirements and identify missing features. |
| Explain this topic.                   | Explain the topic to a beginner and include two practical examples. |
| Test this page.                       | Prepare test scenarios for valid input, invalid input, boundary values, and error conditions. |

A **constraint** is a rule or limitation that the AI must follow.

Examples:
- Use simple language.
- Do not include advanced topics.
- Use only the information provided.
- Do not invent facts.
- Return exactly five examples.
- Present the result in a table.
- Do not include source code in the explanation.

Constraints should be clear and should not contradict one another.

## 6. Output format

Tell the AI how you want the answer to be presented.

Common output formats include:
- Bullet points.
- Numbered steps.
- Tables.
- Short paragraphs.
- Frequently asked questions.
- A checklist.
- A JSON object when a system needs structured data.

**Example**

> Compare manual testing and automation testing. Present the answer in a table with these columns: Feature, Manual Testing, Automation Testing, and Example. Finish with three key points.

Always check whether the response follows the requested format. Asking for a particular format does not guarantee that the response is valid or complete.

## 7. Prompt improvement

Do not accept the first response automatically. Review it and improve the prompt.

**Example**

First prompt:

> Explain database testing.

Possible problem: The answer may be too broad.

Improved prompt:

> Explain database testing to a beginner. Cover the purpose of database testing, data validation, CRUD operations, and one example from a banking application. Use simple language and organize the answer under clear headings.

**Participant activity:** Write a prompt asking an AI tool to explain a technical topic. Improve it by adding the audience, required points, and output format.

---

# Part 2 — Core Prompting Techniques

## 8. Zero-shot prompting

**Meaning:** Zero-shot prompting means asking the AI to complete a task without giving it examples of how the task should be performed.

The prompt contains the instruction and the input, but no sample input-output demonstrations.

**Example**

> Classify the following customer feedback as Positive, Negative, Neutral, or Mixed. Give one short reason.  
> Feedback: “The product quality is good, but delivery took too long.”

**Expected result:** Mixed, because the customer is happy with the product quality but unhappy with the delivery time.

**When should we use it?**
- The task is simple and clearly described.
- The expected result is easy to explain.
- You do not have examples to provide.
- You want to get a quick first result.

**Limitation:** The AI may interpret labels or formatting differently from what you expect. Add more detail or examples if the results are inconsistent.

**Participant practice:** Ask the AI to classify five customer reviews without giving examples. Check whether it uses only the requested categories.

## 9. Few-shot prompting

**Meaning:** Few-shot prompting means giving the AI a small number of examples before asking it to handle a new input.

The examples teach the AI the expected pattern, labels, style, or response format.

**Example**

> Classify support requests as Urgent or Normal.  
> Example 1: “The payment service is unavailable for every customer.” Label: Urgent.  
> Example 2: “Please change the colour of my profile page.” Label: Normal.  
> Now classify this request: “Customers are being charged twice for one order.”

**Expected result:** Urgent, because customers are experiencing an incorrect payment.

**How to choose good examples**
- Use clear and realistic examples.
- Include different types of situations.
- Keep the format consistent.
- Make sure the examples have correct labels.
- Avoid examples that contradict one another.

**When should we use it?** Use few-shot prompting when you need consistent classifications, a specific writing style, or a repeated response pattern.

**Limitation:** Poor examples can teach the wrong pattern. More examples do not always mean better results.

**Participant practice:** Give the AI three examples of Positive, Negative, and Neutral feedback. Then ask it to classify five new comments. Compare the result with zero-shot prompting.

## 10. Structured prompting

**Meaning:** Structured prompting means organizing a prompt into clear sections so the AI understands the task, background, information, rules, and expected response.

A common structure is:
1. Instruction.
2. Context.
3. Input.
4. Output format.
5. Constraints, when required.

**Example: Prepare test scenarios**

> Instruction: Prepare test scenarios for a login page.  
> Context: The application is an online shopping website. Users sign in using an email address and password.  
> Input: Consider the login page and its expected behaviour.  
> Constraints: Include valid and invalid login attempts, empty fields, and password masking.  
> Output format: Present the scenarios in a table with Scenario ID, Test Scenario, Expected Result, and Priority.

**When should we use it?**
- The task has several requirements.
- The AI needs project or business context.
- You want a predictable response structure.
- The output will be reviewed or used by another person.

**Participant practice:** Prepare a structured prompt for an employee management application. Ask the AI to list the functional requirements in a table.

---

# Part 3 — Advanced Prompting Techniques

## 11. Chain-of-thought prompting and multi-step problem solving

**Meaning:** This technique asks the AI to approach a complex task in smaller, ordered steps rather than jumping directly to a final answer.

For classroom work, ask for a concise solution outline, calculations, assumptions, and a final verification. Do not treat a detailed explanation as proof that the answer is correct. Check the result independently.

**Example: Server capacity calculation**

> A web application receives 1,800 requests per minute. One server can handle 15 requests per second. The team wants 20% extra capacity. Calculate how many servers are required. Show the unit conversion, capacity calculation, assumptions, and final answer. Round up to a whole server.

**Expected calculation**
- 1,800 requests per minute = 30 requests per second.
- Add 20% headroom: 30 × 1.20 = 36 requests per second.
- Each server handles 15 requests per second.
- 36 ÷ 15 = 2.4.
- Round up: 3 servers.

This is a simplified planning example. Real production capacity also depends on workload, hardware, response time, and other factors.

**Where is this technique useful?**
- Arithmetic and capacity planning.
- Comparing alternatives.
- Analysing a business problem.
- Breaking a large task into smaller tasks.
- Debugging and troubleshooting.

**Important:** Verify calculations, technical claims, and conclusions. The AI can make mistakes even when its explanation sounds convincing.

**Participant practice:** Ask the AI to calculate a monthly cloud cost from a set of supplied prices. Check each calculation manually.

## 12. Role-based prompting / Persona priming

**Meaning:** Role-based prompting asks the AI to respond from a particular professional perspective.

Examples of roles:
- Teacher.
- Senior software developer.
- QA engineer.
- Security reviewer.
- Technical writer.
- Business analyst.
- Customer support executive.

**Example**

> Act as a QA engineer. Review the requirements for an online banking login page. Identify positive test scenarios, negative test scenarios, security-related scenarios, and usability scenarios. Present the result in a table.

**Another example**

> Act as a technical trainer. Explain the concept of dependency injection to a beginner Java developer. Use a simple real-world analogy and one practical example.

**Why use it?** A role helps focus the response on the responsibilities, vocabulary, and priorities of a particular job.

**Limitation:** Giving the AI a role does not make it a qualified professional or guarantee that its answer is correct. Review important information.

**Participant practice:** Give the same application requirement to the AI three times: once as a business analyst, once as a developer, and once as a QA engineer. Compare the different outputs.

## 13. Context grounding

**Meaning:** Context grounding means providing the relevant source information and instructing the AI to base its answer on that information.

It is useful when the AI must answer questions about a particular project, policy, document, or specification.

**Example**

> Use only the project information below. If the answer is not available, say “Not specified in the supplied information.”  
> Project information: The application uses Python 3.12, FastAPI, and pytest. The project does not allow additional external libraries.  
> Question: Which testing framework does the project use?  
> Return the answer and mention the supporting project detail.

**Expected result:** The project uses pytest.

**Unanswerable question example**

> Which cloud provider hosts this application?

**Expected result:** Not specified in the supplied information.

**When should we use it?**
- Asking questions about project documents.
- Summarizing company policies.
- Analysing requirements.
- Extracting information from reports.
- Working with internal knowledge or RAG applications.

**Limitation:** The AI may still add unsupported details. Compare its answer with the original source.

**Participant practice:** Give the AI a short project description. Ask three questions that can be answered and one question whose answer is missing. Check whether it avoids guessing.

## 14. Reusable prompt patterns for software engineering

A prompt pattern is a reusable prompt structure for a task that occurs frequently. It saves time and helps teams follow a consistent approach.

### 14.1 Code generation prompt pattern

Ask the AI to create a feature based on clearly stated requirements.

**Example**

> Act as a Python developer. I need an employee search feature for an employee management application. Users should be able to search employees by name and department. Explain the required functionality, input validation, possible error conditions, and expected response. Follow the project requirements provided. Do not add features that were not requested.

### 14.2 Test design prompt pattern

Ask the AI to prepare test scenarios from requirements.

**Example**

> Act as a QA engineer. Prepare test scenarios for a money transfer feature in a banking application. Include valid transfers, insufficient balance, invalid account details, zero amount, negative amount, and network failure. Present the scenarios with expected results and priority.

### 14.3 Pull request review prompt pattern

A pull request (PR) review checks proposed code changes before they are merged into a project.

**Example**

> Act as a senior code reviewer. Review the supplied code changes for correctness, security, performance, readability, and maintainability. List only actionable findings. For each finding, explain the problem, its impact, and the suggested improvement. If no issue is found, state that clearly.

### 14.4 Documentation and docstring prompt pattern

A docstring explains the purpose and usage of a function, class, or module.

**Example**

> Act as a technical writer. Prepare documentation for the supplied function. Explain its purpose, input parameters, return value, and exceptions that may occur. Use only information supported by the supplied function. Do not invent behaviour.

### 14.5 Deployment planning prompt pattern

A deployment prompt asks the AI to help prepare a safe deployment plan.

**Example**

> Act as a DevOps engineer. Prepare a deployment checklist for a staging environment. Include prerequisites, configuration checks, deployment steps, health checks, rollback steps, and security precautions. Do not include real passwords, tokens, or credentials. Do not target production.

**Safety reminder:** Review generated code, tests, infrastructure instructions, and deployment steps before using them. Never share secrets with an AI tool or execute generated commands without understanding them.

**Participant practice:** Choose one small application requirement. Prepare separate prompts for feature planning, test design, code review, documentation, and deployment planning.

---

# Part 4 — Prompt Applications

## 15. Synthetic data generation

**Meaning:** Synthetic data is artificial sample data created for learning, demonstrations, testing, or experiments.

An AI model can generate sample customer reviews, employee records, support tickets, product descriptions, or test scenarios.

**Example**

> Generate five fictional customer reviews for an online shopping application. Include two Positive reviews, two Negative reviews, and one Neutral review. Keep each review short. Present the result in a table with Review ID, Review, and Sentiment. Do not repeat the same wording.

**What should we verify?**
- Is the requested number of records correct?
- Is the distribution of labels correct?
- Does each label match the review?
- Are there duplicate or unrealistic records?
- Is any real personal information included?

**Limitation:** Synthetic data may not represent real customer behaviour. Do not use it as a substitute for representative real-world evaluation data.

**Participant practice:** Generate sample feedback for a food delivery application. Ask for different sentiment categories and manually verify the labels.

## 16. RAG data generation

**Meaning of RAG (Retrieval-Augmented Generation) is an approach in which an AI application retrieves relevant information from a knowledge source and provides that information to the language model before it answers.

A simple RAG flow is:

1. A user asks a question.
2. The application searches its knowledge source.
3. Relevant information is retrieved.
4. The retrieved information is given to the AI model.
5. The model prepares an answer using that information.

A training example for RAG commonly contains three parts:

| Part                      | Meaning |
|---------------------------|---------|
| Context                   | The source information or policy passage. |
| Query                     | A question about the context. |
| Answer                    | An answer supported by the context. |

**Example**

> Context: Employees can apply for annual leave through the HR portal. Their manager must approve the request.  
> Query: Where should an employee apply for annual leave?  
> Answer: The employee should apply through the HR portal.

**Unanswerable example**

> Query: How many annual leave days does an employee receive?  
> Answer: Not specified in the supplied context.

**Participant practice:** Create three context-query-answer examples using a fictional IT support policy. Include one question whose answer is not present in the context.

## 17. Prompt templates

**Meaning:** A prompt template is a reusable prompt containing placeholders for information that changes from one request to another.

Instead of writing a new prompt every time, keep the common instruction and replace values such as topic, audience, product, or customer question.

**Example template**

> Explain {TOPIC} to a {AUDIENCE}. Use {LANGUAGE_LEVEL} language and include one practical example.

**Example values**
- TOPIC: REST API.
- AUDIENCE: Beginner Python student.
- LANGUAGE_LEVEL: Simple.

The final prompt becomes:

> Explain REST API to a beginner Python student. Use simple language and include one practical example.

**Benefits**
- Saves time.
- Encourages consistency.
- Makes prompts reusable.
- Makes it easier to test different inputs.

**Participant practice:** Prepare a reusable prompt template for explaining any programming concept to beginners. Test it with Java, Python, and JavaScript topics.

## 18. LangChain prompt-template concepts

LangChain provides ways to prepare reusable prompts for language-model applications. The lesson introduces the following concepts. The purpose here is to understand what each one does before participants practise it with code.

### 18.1 String PromptTemplate

A String PromptTemplate is a reusable text prompt with placeholders. Values are supplied when the application prepares the final prompt.

**Example idea:** A template says, “Explain {TOPIC} to {AUDIENCE}.” The application supplies “Java Streams” as the topic and “beginner Java developer” as the audience.

### 18.2 ChatPromptTemplate

A ChatPromptTemplate prepares a conversation as separate messages with roles.

Common roles include:
- **System:** General behaviour or instructions for the AI.
- **Human:** The user's question or request.
- **AI:** A previous response from the assistant.

**Example idea:** The system message says the AI is a programming tutor. The human message asks it to explain Java collections.

### 18.3 Custom prompt templates

A custom prompt template is a template designed for a particular application or business requirement.

For example, a banking application may use a custom template that always includes the customer's question, relevant policy information, and a rule not to guess missing information.

A well-designed custom template should define the information it needs and handle missing values clearly.

### 18.4 Message prompt templates

Message prompt templates prepare individual messages for a chat conversation. Different message templates can be used for system instructions, human questions, and AI responses.

### 18.5 MessagesPlaceholder

MessagesPlaceholder provides a place in a chat template where a list of previous conversation messages can be inserted.

**Example idea:** A programming tutor may need the last two messages to understand a student's follow-up question.

Only include relevant conversation history. Unnecessary history can confuse the response or expose information that is not needed.

### 18.6 Example selectors

Example selectors choose which examples should be included in a prompt.

For example, a system may have 100 sample customer-support questions but include only the three examples most relevant to the current question.

**Why use them?** They help select useful examples without placing every available example into the prompt.

**Participant practice:** First explain in your own words the difference between a string prompt template and a chat prompt template. Then use the relevant LangChain learning exercise to practise creating and supplying template values.

---

# Part 5 — Prompt Evaluation and Improvement

## 19. Why should prompts be evaluated?

A prompt should not be considered successful because it produced one good answer. It should produce useful results across different inputs.

Prompt evaluation checks:
- Accuracy.
- Completeness.
- Relevance.
- Clarity.
- Output-format compliance.
- Safety and adherence to constraints.
- Consistency across repeated tests.

## 20. Golden test dataset

A golden test dataset is a collection of test inputs with trusted expected results. It is used to check whether a prompt continues to behave correctly.

**Example: Payment status classification**

| Test case | Input                             | Expected result |
|-----------|--------------                     |----------------------------------------|
| 1 |       Payment completed successfully.     | Success |
| 2 |       Payment was declined by the bank.   | Failed |
| 3 |       Payment gateway did not respond.    | Unknown or Pending, depending on the supplied rules |
| 4 |       No payment status was provided.     | Ask for clarification or return Unknown |

Use the same test cases whenever you change the prompt. This helps you compare versions fairly.

**Participant practice:** Prepare five customer-support inputs and write the expected category for each one. Use them to test two versions of the same prompt.

## 21. Expected output and evaluation rubric

An expected output describes what a good response should contain. A rubric is a set of criteria used to score the response.

Example scoring scale:

| Score | Meaning               |
|-------|---------------------  |
| 1 |   Poor — major requirements are missing or incorrect. |
| 2 |   Needs improvement — several problems are present. |
| 3 |   Acceptable — most requirements are met. |
| 4 |   Very good — nearly all requirements are met. |
| 5 |   Excellent — accurate, complete, clear, and follows all instructions. |

Possible evaluation criteria:
- Accuracy: Is the information correct?
- Completeness: Are all requested points covered?
- Clarity: Is the answer easy to understand?
- Relevance: Does the answer stay on the topic?
- Format: Does it follow the requested structure?
- Safety: Does it respect the stated restrictions?

## 22. Human evaluation

Human evaluation means a person reviews the AI response and decides whether it meets the requirements.

It is useful when the quality depends on judgment, such as:
- Whether an explanation is understandable.
- Whether a test plan covers important cases.
- Whether a summary preserves the important information.
- Whether a code review comment is useful.

Use the same evaluation criteria for each response. Record the problems and suggestions for improvement.

## 23. LLM-as-judge

LLM-as-judge means using one AI model to evaluate the response produced by another AI model or prompt.

**Example**

> Evaluate the supplied answer using these criteria: accuracy, completeness, clarity, and relevance. Give each criterion a score from 1 to 5. Explain each score briefly and identify any statement that is not supported by the supplied source.

**Important limitation:** An AI judge can also make mistakes or show bias. It should support human evaluation, not replace it. Check important or high-risk results manually.

## 24. Prompt regression testing

Regression testing checks whether a prompt change has damaged something that worked correctly before.

**Example:** A prompt previously classified payment failures correctly. After adding a new instruction, it starts classifying pending payments as successful. Regression testing helps identify this problem.

Steps:
1. Save the original prompt and its results.
2. Keep a fixed set of test inputs.
3. Change the prompt.
4. Run the same test inputs again.
5. Compare the new results with the expected results.
6. Investigate any failures before accepting the change.

## 25. Prompt versioning

Prompt versioning means maintaining different versions of a prompt and recording how they change.

**Example**

| Version | Change                                  | Reason                        |
|---      |-----------------------|-----------------|
| v1      | Initial prompt                          | Establish a baseline.         |
| v2      | Added a required table format.          | Improve response consistency. |
| v3      | Added rules for missing information.    | Reduce unsupported answers.   |

Record the date, purpose of the change, test results, and the person who reviewed it. Keep an earlier working version so that you can return to it if needed.

## 26. A/B testing prompts

A/B testing compares two prompt versions to identify which one performs better.

**Example**
- Prompt A asks the AI to classify customer feedback using a short instruction.
- Prompt B gives the AI the same instruction plus category definitions and output requirements.

Test both prompts using the same set of customer comments. Compare accuracy, consistency, completeness, response time, and cost where relevant.

Do not decide based on one response. Use enough comparable test cases to make the comparison meaningful.

**Participant practice:** Create two prompt versions for classifying support tickets. Test both with the same ten tickets and compare the results using a simple scoring table.

---

# Part 6 — Building a Personal Prompt Library

## 27. What is a prompt library?

A prompt library is a collection of reusable prompts for tasks that you perform regularly.

A team may maintain prompts for:
- Explaining technical concepts.
- Generating feature requirements.
- Preparing test scenarios.
- Reviewing code changes.
- Writing documentation.
- Summarizing project documents.
- Creating sample test data.
- Preparing deployment checklists.

## 28. What information should a prompt library contain?

| Field                 | Description       |
|-----------------------|-------------------|
| Prompt name           | A short name for the prompt. |
| Purpose               | What task does it perform? |
| Prompt text           | The complete reusable instruction. |
| Required input        | What information must the user provide? |
| Expected output       | What should the AI return? |
| Constraints           | What rules must the AI follow? |
| Version               | Current prompt version. |
| Evaluation status     | Draft, tested, or validated. |
| Notes                 | Known limitations and review comments. |

A prompt should be marked **validated** only after its results have been checked against requirements and representative test cases.

## 29. Example personal prompt library

A beginner software team could maintain these prompts:

1. **Requirement explanation:** Explain a feature requirement in simple language.
2. **Test scenario preparation:** Prepare positive, negative, and boundary test scenarios.
3. **Code review:** Identify actionable issues in a proposed code change.
4. **Documentation:** Explain the purpose, inputs, outputs, and exceptions of a function.
5. **Troubleshooting:** Analyse an error message and suggest checks in a safe order.

**Participant activity:** Create a small prompt library containing at least five prompts. Test each prompt with sample input and record one improvement.

---

# Part 7 — Final Practical Workshop

## 30. Capstone activity: Prompt engineering for an employee support application

**Scenario**

A company is planning an employee support application. Employees can ask questions about leave, attendance, payroll, and IT support.

Participants must prepare prompts for the following tasks:

1. Ask the AI to explain the application requirements.
2. Ask the AI to classify employee support requests.
3. Give examples and use few-shot prompting to improve classification consistency.
4. Ask the AI to prepare test scenarios for the support request feature.
5. Provide a short policy document and use context grounding to answer employee questions.
6. Generate fictional sample support requests.
7. Prepare context-query-answer examples for a simple RAG exercise.
8. Create a reusable prompt template for answering employee questions.
9. Evaluate the responses using a golden test dataset and rubric.
10. Compare two prompt versions and record which one performs better.

**Submission checklist**

- [ ] Five or more clearly written prompts.
- [ ] At least one zero-shot prompt.
- [ ] At least one few-shot prompt.
- [ ] At least one structured prompt using instruction, context, input, and output format.
- [ ] At least one role-based prompt.
- [ ] At least one context-grounded prompt.
- [ ] One synthetic dataset or RAG example set.
- [ ] A small evaluation dataset with expected results.
- [ ] A comparison of two prompt versions.
- [ ] Notes describing what was improved and why.

## 31. Common mistakes to avoid

- Giving a very broad instruction.
- Forgetting to explain the target audience.
- Not providing necessary project context.
- Giving examples that are incorrect or inconsistent.
- Asking for an output format but not checking it.
- Assuming that an AI-generated answer is always correct.
- Asking the AI to guess missing project information.
- Sharing passwords, API keys, or confidential data.
- Using generated code or deployment instructions without review.
- Changing a prompt without testing whether the change caused a regression.

## 32. Key takeaways

- A prompt is an instruction or request given to an AI model.
- Good prompts clearly describe the task and expected result.
- Zero-shot prompting uses no examples; few-shot prompting includes examples.
- Structured prompting organizes the instruction, context, input, and output.
- Reasoning-oriented prompts can help with multi-step tasks, but answers must be verified.
- Role-based prompting focuses the response on a particular perspective.
- Context grounding helps the AI answer using supplied information.
- Prompt patterns and templates make repeated tasks easier.
- Prompt evaluation helps measure quality and consistency.
- A prompt library helps individuals and teams reuse and improve their work.

**Final message for participants:** Understand the problem first. Write the prompt clearly. Test the response. Verify the result. Improve the prompt. Then use the AI-generated output responsibly.
