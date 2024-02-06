# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START functions_cloudevent_storage_unit_test]

from cloudevents.http import CloudEvent
import pytest

import main

def test_functions_eventsource_storage(capsys: pytest.LogCaptureFixture) -> None:
    attributes = {
        "id": "5e9f24a",
        "type": "google.cloud.storage.object.v1.finalized",
        "source": "sourceUrlHere",
        "subject": "pathToFile"
    }

    data = {
        "bucket": "test_bucket_for_storage",
        "name": "new_blob_uploaded",
        "generation": 1,
        "metageneration": 1,
        "timeCreated": "2021-10-10 00:00:00.000000Z",
        "updated": "2021-11-11 00:00:00.000000Z",
    }
    event = CloudEvent(attributes, data)
    is_success = main.gcs_ingestion(event)
    assert is_success

# [END functions_cloudevent_storage_unit_test]