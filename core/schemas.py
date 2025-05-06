from typing import List, Dict, Union
from pydantic import BaseModel, Field
from enum import Enum

class ArchitecturePattern(str, Enum):
    MICROSERVICES = "microservices"
    MONOLITHIC = "monolithic"
    SERVERLESS = "serverless"
    EVENT_DRIVEN = "event_driven"

class DatabaseType(str, Enum):
    SQL = "sql"
    NOSQL = "nosql"
    HYBRID = "hybrid"

class ComplianceStandard(str, Enum):
    HIPAA = "hipaa"
    GDPR = "gdpr"
    SOC2 = "soc2"
    ISO27001 = "iso27001"

class ArchitectureDecision(BaseModel):
    pattern: ArchitecturePattern
    rationale: str = Field(..., min_length=50)
    trade_offs: Dict[str, List[str]]
    estimated_cost: Dict[str, float]

class SecurityMeasure(BaseModel):
    measure_type: str
    implementation_priority: int = Field(..., ge=1, le=5)
    compliance_standards: List[ComplianceStandard]
    data_classification: str

class InfrastructureResource(BaseModel):
    resource_type: str
    specifications: Dict[str, str]
    scaling_policy: Dict[str, str]
    estimated_cost: float

class TechnicalAnalysis(BaseModel):
    architecture_decision: ArchitectureDecision
    infrastructure_resources: List[InfrastructureResource]
    security_measures: List[SecurityMeasure]
    database_choice: DatabaseType
    compliance_requirements: List[ComplianceStandard] = []
    performance_requirements: List[Dict[str, Union[str, float]]] = []
    risk_assessment: Dict[str, str] = {}
