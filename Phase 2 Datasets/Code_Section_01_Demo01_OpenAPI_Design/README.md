# Cisco / Simplilearn — M2S1 Demo 01 Source Files
## Design and Validate a REST API Contract with OpenAPI

These files correspond to the *existing screenshots and sequence* in the demo guide.

| Demo screenshot | File to open | What learners do |
|---|---|---|
| Step 1: REST URI design (page 2) | `M2S1_REST_URI_DESIGN.md` | Review the three endpoint routes |
| Step 2: Starter YAML (page 3) | `device_management_openapi_starter.yaml` | Open in VS Code; examine `openapi`, `info`, `paths` |
| Step 3: GET /devices (page 4) | `device_management_openapi_final.yaml` | Examine `get`, response 200, array and Device schema |
| Step 4: POST /devices (pages 4–5) | `device_management_openapi_final.yaml` | Examine requestBody, DeviceCreate and 201 |
| Step 5: GET /devices/{device_id} (page 6) | `device_management_openapi_final.yaml` | Examine path parameter and responses 200/404 |
| Steps 6–7: Swagger Editor (pages 7–8) | `device_management_openapi_final.yaml` | Copy whole YAML into https://editor.swagger.io/ and inspect three operations |
| Step 8: REST review (page 9) | `M2S1_REST_DESIGN_REVIEW.md` | Discuss contract design checklist |

## Exact beginner walkthrough
1. Open VS Code and use **File > Open Folder** to select this folder.
2. Open `M2S1_REST_URI_DESIGN.md` to identify the resource and three method/URI pairs.
3. Open `device_management_openapi_starter.yaml` and point out the three top-level keys.
4. Open `device_management_openapi_final.yaml` and compare it with the starter file.
5. Point out `GET /devices`, its response `200`, and a list (`type: array`) of `Device` objects.
6. Point out `POST /devices`, its JSON `requestBody`, and response `201`.
7. Point out `GET /devices/{device_id}`, its required integer `device_id`, and responses `200`/`404`.
8. Press **Ctrl+A**, **Ctrl+C** while the final YAML is active. Open https://editor.swagger.io/ in Chrome, select the left editor text and paste the final YAML. If asked to replace the sample definition, confirm.
9. Confirm the right pane lists **GET /devices**, **POST /devices**, and **GET /devices/{device_id}**. Expand POST to inspect the request body schema.
10. Open `M2S1_REST_DESIGN_REVIEW.md` and discuss all six checks.

**No API server is started or implemented in this exercise.** Swagger Editor documents a contract; "Try it out" is not a functional backend test without a running service.

## Faithfulness note
The endpoint paths, operation summaries, method choices, response codes, and schema names (`Device`, `DeviceCreate`) follow the supplied demo. The screenshots do not reliably establish every schema field and detailed example, so the final YAML uses illustrative `name`, `status`, and `id` fields and an illustrative device ID of `101`. The original contract may have used a different exact schema structure. The screenshot flow is preserved; these illustrative fields make the standalone YAML complete and useful.

## Expected YAML validation
The complete YAML should render in Swagger Editor with three operations and schemas under the Schemas section. It only validates API description structure, not business behavior.
