#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import copy
import mock
import random
import uuid

from openstackclient.common import utils as common_utils
from openstackclient.tests import fakes
from openstackclient.tests.identity.v3 import fakes as identity_fakes
from openstackclient.tests.image.v2 import fakes as image_fakes
from openstackclient.tests import utils

volume_attachment_server = {
    'device': '/dev/ice',
    'server_id': '1233',
}

volume_id = "ce26708d-a7f8-4b4b-9861-4a80256615a6"
volume_name = "fake_volume"
volume_description = "fake description"
volume_status = "available"
volume_size = 20
volume_type = "fake_lvmdriver-1"
volume_metadata = {
    'Alpha': 'a',
    'Beta': 'b',
    'Gamma': 'g',
}
volume_metadata_str = "Alpha='a', Beta='b', Gamma='g'"
volume_snapshot_id = 1
volume_availability_zone = "nova"
volume_attachments = [volume_attachment_server]

VOLUME = {
    "id": volume_id,
    "name": volume_name,
    "description": volume_description,
    "status": volume_status,
    "size": volume_size,
    "volume_type": volume_type,
    "metadata": volume_metadata,
    "snapshot_id": volume_snapshot_id,
    "availability_zone": volume_availability_zone,
    "attachments": volume_attachments
}

VOLUME_columns = (
    "attachments",
    "availability_zone",
    "description",
    "id",
    "name",
    "properties",
    "size",
    "snapshot_id",
    "status",
    "type"
)

VOLUME_data = (
    volume_attachments,
    volume_availability_zone,
    volume_description,
    volume_id,
    volume_name,
    common_utils.format_dict(volume_metadata),
    volume_size,
    volume_snapshot_id,
    volume_status,
    volume_type
)


snapshot_id = "cb2d364e-4d1c-451a-8c68-b5bbcb340fb2"
snapshot_name = "fake_snapshot"
snapshot_description = "fake description"
snapshot_size = 10
snapshot_metadata = {
    "foo": "bar"
}
snapshot_volume_id = "bdbae8dc-e6ca-43c0-8076-951cc1b093a4"

SNAPSHOT = {
    "id": snapshot_id,
    "name": snapshot_name,
    "description": snapshot_description,
    "size": snapshot_size,
    "status": "available",
    "metadata": snapshot_metadata,
    "created_at": "2015-06-03T18:49:19.000000",
    "volume_id": volume_name
}
EXPECTED_SNAPSHOT = copy.deepcopy(SNAPSHOT)
EXPECTED_SNAPSHOT.pop("metadata")
EXPECTED_SNAPSHOT['properties'] = "foo='bar'"
SNAPSHOT_columns = tuple(sorted(EXPECTED_SNAPSHOT))
SNAPSHOT_data = tuple((EXPECTED_SNAPSHOT[x]
                       for x in sorted(EXPECTED_SNAPSHOT)))


type_id = "5520dc9e-6f9b-4378-a719-729911c0f407"
type_description = "fake description"
type_name = "fake-lvmdriver-1"
type_extra_specs = {
    "foo": "bar"
}

TYPE = {
    'id': type_id,
    'name': type_name,
    'description': type_description,
    'extra_specs': type_extra_specs
}

TYPE_columns = tuple(sorted(TYPE))
TYPE_data = tuple((TYPE[x] for x in sorted(TYPE)))

formatted_type_properties = "foo='bar'"
TYPE_FORMATTED = {
    'id': type_id,
    'name': type_name,
    'description': type_description,
    'properties': formatted_type_properties
}
TYPE_FORMATTED_columns = tuple(sorted(TYPE_FORMATTED))
TYPE_FORMATTED_data = tuple((TYPE_FORMATTED[x] for x in
                             sorted(TYPE_FORMATTED)))

backup_id = "3c409fe6-4d03-4a06-aeab-18bdcdf3c8f4"
backup_volume_id = "bdbae8dc-e6ca-43c0-8076-951cc1b093a4"
backup_name = "fake_backup"
backup_description = "fake description"
backup_object_count = None
backup_container = None
backup_size = 10
backup_status = "error"

BACKUP = {
    "id": backup_id,
    "name": backup_name,
    "volume_id": backup_volume_id,
    "description": backup_description,
    "object_count": backup_object_count,
    "container": backup_container,
    "size": backup_size,
    "status": backup_status,
    "availability_zone": volume_availability_zone,
}

BACKUP_columns = tuple(sorted(BACKUP))
BACKUP_data = tuple((BACKUP[x] for x in sorted(BACKUP)))

qos_id = '6f2be1de-997b-4230-b76c-a3633b59e8fb'
qos_consumer = 'front-end'
qos_default_consumer = 'both'
qos_name = "fake-qos-specs"
qos_specs = {
    'foo': 'bar',
    'iops': '9001'
}
qos_association = {
    'association_type': 'volume_type',
    'name': type_name,
    'id': type_id
}

QOS = {
    'id': qos_id,
    'consumer': qos_consumer,
    'name': qos_name
}

QOS_DEFAULT_CONSUMER = {
    'id': qos_id,
    'consumer': qos_default_consumer,
    'name': qos_name
}

QOS_WITH_SPECS = {
    'id': qos_id,
    'consumer': qos_consumer,
    'name': qos_name,
    'specs': qos_specs
}

QOS_WITH_ASSOCIATIONS = {
    'id': qos_id,
    'consumer': qos_consumer,
    'name': qos_name,
    'specs': qos_specs,
    'associations': [qos_association]
}

image_id = 'im1'
image_name = 'graven'
IMAGE = {
    'id': image_id,
    'name': image_name
}

extension_name = 'SchedulerHints'
extension_namespace = 'http://docs.openstack.org/'\
    'block-service/ext/scheduler-hints/api/v2'
extension_description = 'Pass arbitrary key/value'\
    'pairs to the scheduler.'
extension_updated = '2013-04-18T00:00:00+00:00'
extension_alias = 'OS-SCH-HNT'
extension_links = '[{"href":'\
    '"https://github.com/openstack/block-api", "type":'\
    ' "text/html", "rel": "describedby"}]'

EXTENSION = {
    'name': extension_name,
    'namespace': extension_namespace,
    'description': extension_description,
    'updated': extension_updated,
    'alias': extension_alias,
    'links': extension_links,
}


class FakeVolumeClient(object):

    def __init__(self, **kwargs):
        self.volumes = mock.Mock()
        self.volumes.resource_class = fakes.FakeResource(None, {})
        self.volume_snapshots = mock.Mock()
        self.volume_snapshots.resource_class = fakes.FakeResource(None, {})
        self.backups = mock.Mock()
        self.backups.resource_class = fakes.FakeResource(None, {})
        self.volume_types = mock.Mock()
        self.volume_types.resource_class = fakes.FakeResource(None, {})
        self.volume_type_access = mock.Mock()
        self.volume_type_access.resource_class = fakes.FakeResource(None, {})
        self.restores = mock.Mock()
        self.restores.resource_class = fakes.FakeResource(None, {})
        self.qos_specs = mock.Mock()
        self.qos_specs.resource_class = fakes.FakeResource(None, {})
        self.availability_zones = mock.Mock()
        self.availability_zones.resource_class = fakes.FakeResource(None, {})
        self.auth_token = kwargs['token']
        self.management_url = kwargs['endpoint']


class TestVolume(utils.TestCommand):

    def setUp(self):
        super(TestVolume, self).setUp()

        self.app.client_manager.volume = FakeVolumeClient(
            endpoint=fakes.AUTH_URL,
            token=fakes.AUTH_TOKEN
        )
        self.app.client_manager.identity = identity_fakes.FakeIdentityv3Client(
            endpoint=fakes.AUTH_URL,
            token=fakes.AUTH_TOKEN
        )
        self.app.client_manager.image = image_fakes.FakeImagev2Client(
            endpoint=fakes.AUTH_URL,
            token=fakes.AUTH_TOKEN
        )


class FakeVolume(object):
    """Fake one or more volumes.

    TODO(xiexs): Currently, only volume API v2 is supported by this class.
    """

    @staticmethod
    def create_one_volume(attrs={}):
        """Create a fake volume.

        :param Dictionary attrs:
            A dictionary with all attributes of volume
        :retrun:
            A FakeResource object with id, name, status, etc.
        """
        # Set default attribute
        volume_info = {
            'id': 'volume-id' + uuid.uuid4().hex,
            'name': 'volume-name' + uuid.uuid4().hex,
            'description': 'description' + uuid.uuid4().hex,
            'status': random.choice(['available', 'in_use']),
            'size': random.randint(1, 20),
            'volume_type':
                random.choice(['fake_lvmdriver-1', 'fake_lvmdriver-2']),
            'metadata': {
                'key' + uuid.uuid4().hex: 'val' + uuid.uuid4().hex,
                'key' + uuid.uuid4().hex: 'val' + uuid.uuid4().hex,
                'key' + uuid.uuid4().hex: 'val' + uuid.uuid4().hex},
            'snapshot_id': random.randint(1, 5),
            'availability_zone': 'zone' + uuid.uuid4().hex,
            'attachments': [{
                'device': '/dev/' + uuid.uuid4().hex,
                'server_id': uuid.uuid4().hex,
            }, ],
        }

        # Overwrite default attributes if there are some attributes set
        volume_info.update(attrs)

        volume = fakes.FakeResource(
            None,
            volume_info,
            loaded=True)
        return volume

    @staticmethod
    def create_volumes(attrs={}, count=2):
        """Create multiple fake volumes.

        :param Dictionary attrs:
            A dictionary with all attributes of volume
        :param Integer count:
            The number of volumes to be faked
        :return:
            A list of FakeResource objects
        """
        volumes = []
        for n in range(0, count):
            volumes.append(FakeVolume.create_one_volume(attrs))

        return volumes

    @staticmethod
    def get_volumes(volumes=None, count=2):
        """Get an iterable MagicMock object with a list of faked volumes.

        If volumes list is provided, then initialize the Mock object with the
        list. Otherwise create one.

        :param List volumes:
            A list of FakeResource objects faking volumes
        :param Integer count:
            The number of volumes to be faked
        :return
            An iterable Mock object with side_effect set to a list of faked
            volumes
        """
        if volumes is None:
            volumes = FakeVolume.create_volumes(count)

        return mock.MagicMock(side_effect=volumes)


class FakeAvailabilityZone(object):
    """Fake one or more volume availability zones (AZs)."""

    @staticmethod
    def create_one_availability_zone(attrs={}, methods={}):
        """Create a fake AZ.

        :param Dictionary attrs:
            A dictionary with all attributes
        :param Dictionary methods:
            A dictionary with all methods
        :return:
            A FakeResource object with zoneName, zoneState, etc.
        """
        # Set default attributes.
        availability_zone = {
            'zoneName': uuid.uuid4().hex,
            'zoneState': {'available': True},
        }

        # Overwrite default attributes.
        availability_zone.update(attrs)

        availability_zone = fakes.FakeResource(
            info=copy.deepcopy(availability_zone),
            methods=methods,
            loaded=True)
        return availability_zone

    @staticmethod
    def create_availability_zones(attrs={}, methods={}, count=2):
        """Create multiple fake AZs.

        :param Dictionary attrs:
            A dictionary with all attributes
        :param Dictionary methods:
            A dictionary with all methods
        :param int count:
            The number of AZs to fake
        :return:
            A list of FakeResource objects faking the AZs
        """
        availability_zones = []
        for i in range(0, count):
            availability_zone = \
                FakeAvailabilityZone.create_one_availability_zone(
                    attrs, methods)
            availability_zones.append(availability_zone)

        return availability_zones
